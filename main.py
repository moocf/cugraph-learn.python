#!/usr/bin/env python3
from random import random, randrange
import numpy as np
import cudf
import cugraph


# constants
REC0 = 5   # recovery time range start
REC1 = 15  # recovery time range end
INF0 = 10  # infection time range start
INF1 = 20  # infection time range end
EDGP = 0.2 # edge probability
SRC = 0    # source of infection


def contactGraph(N):
    v = cudf.DataFrame()
    v['id'] = [i for i in range(N)]
    v['wt'] = [randrange(REC0, REC1) for i in range(N)]
    el = []
    for i in range(N):
        for j in range(N):
            if j != i and random() <= EDGP:
                wt = randrange(REC0, REC1)
                el.append((i, j, wt))
    e = cudf.DataFrame(el, columns=['src', 'dst', 'wt'])
    return (v, e)


def infectableGraph(v, e):
    f = cudf.DataFrame()
    f['vwt'] = v['wt'][e['src']].to_arrow().to_pylist()
    return e[e['wt'] > f['vwt']]


def pathGraph(e):
    if e.empty:
        return e
    g = cugraph.Graph()
    g.from_cudf_edgelist(e, source='src', destination='dst', edge_attr='wt')
    d = cugraph.shortest_path(g, SRC)
    return d[d['distance'] < 1e+38]


# main
v, e = contactGraph(5)
print('Contact Graph:   ', v.shape, e.shape)

f = infectableGraph(v, e)
print('Infectable Graph:', v.shape, f.shape)

d = pathGraph(f)
print('Path graph:      ', v.shape, d.shape)

print(f)
print(d)

# for i in range(len(d)):
#     print('vertex ' + str(d['vertex'].iloc[i]) + ' distance is ' + str(d['distance'].iloc[i]))
# csv = 'data/min2d.csv'
# data = cudf.read_csv(csv, names=['src', 'dst', 'wt'], dtype=['int32', 'int32', 'float32'])
