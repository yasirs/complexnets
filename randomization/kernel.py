# trying out graph diffusion kernel

import rewire
import numpy as np
import numpy.linalg
import networkx as nx

G = rewire.readBiogrid('BIOGRID-ORGANISM-Bos_taurus-3.2.108.tab2.txt')
zero_degree_nodes = [n for (n,d) in G.degree_iter() if d==0]
G.remove_nodes_from(zero_degree_nodes)
A = nx.to_numpy_matrix(G)
node_names = G.nodes()
W = A/A.sum(axis=0)
n = G.number_of_nodes()
L = np.eye(n) - W*(1-.05)
K = numpy.linalg.inv(L)
Q = np.zeros(n)
Q[0]=1; Q[1]=1; Q[2]=1
V = Q*K
V = V.tolist()[0]
V_with_name = [(node_names[i],V[i]) for i in xrange(n)]
V_sorted = sorted(V_with_name, key=lambda x:x[1], reverse=True)
V_sorted[:10]

import pylab
pylab.plot(V,'.')
pylab.show()
