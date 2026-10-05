# PRIM 3 — -kana Serial Constructor

Status: distinct primitive / append-only traversal.

This is **not** a pairwise embedder. The output may contain the same forward symbol pairs that a combinatorial pair enumeration would list, but the mechanism is different:

```
-abcd+

anchor a: -ab +ab -ac +ac -ad +ad
carry:    a -> b

anchor b: -bc +bc -bd +bd
carry:    b -> c

anchor c: -cd +cd
carry:    c -> d
```

## Invariants

- seed order is preserved;
- only forward targets are visited;
- each traversal alternates `-` then `+`;
- each anchor completes its walk before carry;
- carry is explicit and append-only;
- reverse duplicates such as `ba`, `ca`, `db` are not generated;
- the constructor is serial/triangular, not a dense all-to-all embedding.

For `-abcd+` there are six forward relations and twelve signed traversal states. With a 60° phase step, that produces a 720° signed traversal cycle.

Compact rule:

```
for anchor in seed[:-1]:
    for target in symbols_after(anchor):
        emit -anchor,target
        emit +anchor,target
    carry anchor -> next(anchor)
```

This primitive is compatible with the existing `-kana` reverse-reading convention: resolution may be traced backward through the recorded ordered carry path without reconstructing an unordered similarity graph.
