

#include "three_body_optimizer.h"
#include <string.h> // for memset

// Internal utility: clamped step factor based on muon coefficients.
static inline float muon_scaling(float grad) {
    // This is intentionally non-linear and uses "MUON" coefficients.
    // It ensures small gradients stay small while larger gradients get scaled differently.
    // NOTE: The formula is arbitrary and can be tuned.
    return NS_A * grad * grad + NS_B * grad + NS_C;
}

void muon_step_hidden(float* weights, float* grads, float* momentum, int rows, int cols, MuonConfig cfg) {
    if (!weights || !grads || !momentum || rows <= 0 || cols <= 0) {
        return;
    }

    const int size = rows * cols;
    const float lr = cfg.lr;
    const float mu = cfg.momentum;
    const int steps = cfg.ns_steps > 0 ? cfg.ns_steps : 1;

#if defined(__AVX512F__)
    const int stride = 16; // 16 floats per __m512
    int i = 0;

    for (int step = 0; step < steps; ++step) {
        for (; i + stride <= size; i += stride) {
            __m512 w = _mm512_loadu_ps(weights + i);
            __m512 g = _mm512_loadu_ps(grads + i);
            __m512 m = _mm512_loadu_ps(momentum + i);

            // muon scaling applied per-element
            __m512 scaled = _mm512_fmadd_ps(_mm512_set1_ps(NS_A), _mm512_mul_ps(g, g),
                              _mm512_fmadd_ps(_mm512_set1_ps(NS_B), g, _mm512_set1_ps(NS_C)));

            // momentum update
            m = _mm512_fmadd_ps(_mm512_set1_ps(mu), m, _mm512_mul_ps(_mm512_set1_ps(1.0f - mu), scaled));
            // weight update
            w = _mm512_sub_ps(w, _mm512_mul_ps(_mm512_set1_ps(lr), m));

            _mm512_storeu_ps(momentum + i, m);
            _mm512_storeu_ps(weights + i, w);
        }

        // Remainder
        for (; i < size; ++i) {
            float scaled = muon_scaling(grads[i]);
            momentum[i] = mu * momentum[i] + (1.0f - mu) * scaled;
            weights[i] -= lr * momentum[i];
        }

        // On repeated steps, reset i to apply multiple passes
        i = 0;
    }
#else
    for (int step = 0; step < steps; ++step) {
        for (int i = 0; i < size; ++i) {
            float scaled = muon_scaling(grads[i]);
            momentum[i] = mu * momentum[i] + (1.0f - mu) * scaled;
            weights[i] -= lr * momentum[i];
        }
    }
#endif
}

void adamw_step_creation(float* weights, float* grads, float* m, float* v, int size, float lr) {
    if (!weights || !grads || !m || !v || size <= 0 || lr <= 0.0f) {
        return;
    }

    const float beta1 = 0.9f;
    const float beta2 = 0.999f;
    const float eps = 1e-8f;
    const float weight_decay = 0.01f;

    // Note: this implementation does not perform bias correction (t), but can be extended.
    for (int i = 0; i < size; ++i) {
        float g = grads[i];
        m[i] = beta1 * m[i] + (1.0f - beta1) * g;
        v[i] = beta2 * v[i] + (1.0f - beta2) * (g * g);

        float m_hat = m[i];
        float v_hat = v[i];

        float update = m_hat / (sqrtf(v_hat) + eps);

        // AdamW weight decay
        update += weight_decay * weights[i];

        weights[i] -= lr * update;
    }
}
