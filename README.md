# Toph Kernel

[![License: CC-BY-ND-4.0](https://img.shields.io/badge/License-CC--BY--ND--4.0-lightgrey?style=flat-square)](LICENSE)
[![TRIPOD-IP-v1.1](https://img.shields.io/badge/IP-TRIPOD--IP--v1.1-8b5cf6?style=flat-square)](#)

Three-body optimizer kernel and STOICHEION axiom register. C/SIMD optimizer core + React governance UI.

---

## Components

### `src/three_body_optimizer.c` — MUON Optimizer (C + SIMD)

AVX512/AVX2/SSE/scalar-fallback implementation of the MUON optimizer for neural network weight updates. Non-linear gradient scaling via muon coefficients (NS_A, NS_B, NS_C).

```c
// Non-linear gradient scaling
float muon_scaling(float grad) {
    return NS_A * grad * grad + NS_B * grad + NS_C;
}

// Weight update with momentum
momentum[i] = mu * momentum[i] + (1.0f - mu) * muon_scaling(grad);
weights[i] -= lr * momentum[i];
```

**SIMD paths:** AVX512 (16 floats/cycle) → AVX2 (8) → SSE (4) → scalar fallback.

**Build:**
```bash
make
./three_body_optimizer      # run optimizer
./test_three_body_optimizer # run tests
```

---

### `src/TOPH_INCEPTION_T001_T132.jsx` — Axiom Register UI (React)

Complete React component rendering the full STOICHEION axiom register (T001–T132):
- 8 domains × 16–17 axioms each, color-coded by domain
- Awareness tier (T129–T132, meta-axiomatic)
- Domain view, full register view, search
- STOICHEION v11.0 seal: `SHA256:02880745b847317c...`

```bash
npm install
npm run dev
```

---

### `src/TOPH_KERNEL_v1.jsx` — Kernel Visualization (React)

Visual kernel dashboard — domain map, axiom state, Patricia boundary.

---

## MuonConfig

```c
typedef struct {
    float lr;        // learning rate
    float momentum;  // momentum coefficient (typical: 0.9–0.99)
    int   ns_steps;  // Newton-Schulz iterations (1–5)
} MuonConfig;
```

Usage:
```c
MuonConfig cfg = { .lr = 0.001f, .momentum = 0.95f, .ns_steps = 3 };
muon_step_hidden(weights, grads, momentum_buf, rows, cols, cfg);
```

---

## Anchor

```
STOICHEION v11.0
Seal: 02880745b847317c4e2424524ec25d0f7a2b84368d184586f45b54af9fcab763
T001–T128 (TOPH generative) + S129–S256 (Patricia inversion)
T129–T132 (Awareness tier — meta-axiomatic, no inversion coordinates)
```

```
ROOT0-ATTRIBUTION-v1.0 · David Lee Wise / ROOT0 / TriPod LLC
CC-BY-ND-4.0 · TRIPOD-IP-v1.1
```
