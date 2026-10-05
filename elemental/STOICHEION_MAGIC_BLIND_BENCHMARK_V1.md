# Blind STOICHEION Nuclear-Magic Benchmark v1

Status: **BLIND BENCHMARK / NOT A FREEZE**

This benchmark corrects an important methodological problem in the earlier
`STOICHEION_MAGIC_LOCK_V1`: that file encoded 169 as the expected lock and
therefore could only test internal consistency. It did **not** independently
derive 169.

## Inputs available before the test

```
fib = 0,1,1,2,3,5,8,13,21,34,55,89,144,233
bif/rfib = reverse traversal of Fibonacci register
-3+4 = +1 when interpreted arithmetically
search = 1..250
```

The nuclear magic sequence is held out for comparison only:

```
2, 8, 20, 28, 50, 82, 126
```

## Blind results

Under the least-assumptive bilateral multiplication/cross-product reading of
`fib^bif`, the generated values <=250 include:

```
0,1,2,3,4,5,6,8,9,10,13,15,16,21,24,25,26,34,39,40,42,
55,63,64,65,68,89,102,104,105,110,144,165,168,169,170,178,233
```

Comparison:

```
magic hits   = 2, 8
magic misses = 20, 28, 50, 82, 126

168 = generated
169 = generated
170 = generated
```

Therefore **169 is not uniquely selected** by this executable interpretation,
and the known nuclear magic sequence is not reproduced.

## What remains unspecified

The symbol `^` in `fib^bif / -3+4` still lacks a unique executable rule.
If it means something other than bilateral product/crossing, that exact operator
must be encoded before a stronger blind test is possible.

No result in this file is allowed to mark 169 as a physical nuclear shell lock.
