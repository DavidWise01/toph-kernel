










#ifndef THREE_BODY_OPTIMIZER_H
#define THREE_BODY_OPTIMIZER_H

#include <immintrin.h> // For AVX-512 Power (-1)
#include <math.h>

// MUON COEFFICIENTS: 3/2/1 DERIVATIVE
#define NS_A 3.4445f  // +1 WILL: INTENT
#define NS_B -4.7750f // 0 PROBABILITY: ITERATION
#define NS_C 2.0315f  // -1 POWER: EXECUTION

typedef struct {
    float lr;
    float momentum;
    int ns_steps; // Typically 5
} MuonConfig;

/**
 * BODY 1 (+1 WILL): MUON FOR HIDDEN MATRICES
 * This is the "Architect's Layer" where we enforce orthogonality.
 */
void muon_step_hidden(float* weights, float* grads, float* momentum, int rows, int cols, MuonConfig cfg);

/**
 * BODY 2 (0 PROBABILITY): ADAMW FOR CREATION LAYERS
 * This is the "Primordial Soup" for 1D vectors (Biases/Embeddings).
 */
void adamw_step_creation(float* weights, float* grads, float* m, float* v, int size, float lr);

#endif
