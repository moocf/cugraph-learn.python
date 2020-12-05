#!/usr/bin/env python3
import cugraph

data = cudf.read_csv('min2d.csv', names=['src', 'dst', 'wt'], dtype=['int32', 'int32', 'float32'])

G = cugraph.Graph()
G.from_cudf_edgelist(data, source='src', destination='dst', edge_attr='wt')

dist = cugraph.shortest_path(G, 1)
for i in range(len(dist)):
  print('vertex ' + str(dist['vertex'].iloc[i]) + ' distance is ' + str(dist['distance'].iloc[i]))
