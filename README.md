The RAPIDS cuGraph library is a collection of GPU accelerated graph
algorithms that process data found in GPU DataFrames.

**Research**: Infectious Disease Modeling, Monsoon 2020<br>
**Guided by**: Prof. Kishore Kothapalli, Prof. Sriram Pemmaraju
<br>

See [Colaboratory] for notebook, but it takes about *15min* to setup Rapid's
**cuGraph** onto it, before starting. [BlazingSQL] has cuGraph already setup
onto it, but you need to write your own notebook (it has no share feature).
With BlazingSQL you need to copy `data` as well and `main.py` into its
environment.

[Colaboratory]: https://colab.research.google.com/drive/1UX18VehsMOMvv-1_Xo4uYUmqAs7STW5E?usp=sharing
[BlazingSQL]: https://app.blazingsql.com/

<br>

```bash
## OUTPUT
## Small graph: 5 vertices, 5 edges
Contact Graph:    (5, 2) (5, 3)
Infectable Graph: (5, 2) (2, 3)
Path graph:       (5, 2) (3, 3)
   src  dst  wt
1    0    2  10
2    3    0   9
   distance  vertex  predecessor
0       9.0       3            0
1      10.0       2            0
2       0.0       0           -1
```

```bash
## OUTPUT
## Large graph: 50000 vertices, 249272 edges
Contact Graph:    (50000, 2) (249272, 3)
Infectable Graph: (50000, 2) (112381, 3)
Path graph:       (50000, 2) (48619, 3)
```

<br>


### references

- [RAPIDS cuGraph library](https://github.com/rapidsai/cugraph)
- [RAPIDS cuDF library](https://github.com/rapidsai/cudf)
- [cugraph.sssp reference](https://docs.rapids.ai/api/cugraph/stable/api.html#cugraph.traversal.sssp.sssp)

![](https://ga-beacon.deno.dev/G-G1E8HNDZYY:v51jklKGTLmC3LAZ4rJbIQ/github.com/moocf/cugraph-learn.python)
