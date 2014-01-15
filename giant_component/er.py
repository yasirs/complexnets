"""
Created on Sun Jan 05 21:49:09 2014

@author: Yasir Suhail
"""
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

N = 500

num_comps = []
big_comp = []
ps = []


for p in [.11/N, .5/N, .7/N, .9/N, 1.0/N, 1.1/N, 1.5/N, 2.0/N, 3.5/N, 4.0/N, 8.0/N, 10.0/N, 20.0/N, 50.0/N, 1]:
    for i in xrange(10):
        g = nx.random_graphs.erdos_renyi_graph(N,p)
        components = nx.connected_components(g)
        num_comps.append(len(components))
        big_comp.append(len(components[0]))
        ps.append(p)
        

num_comps = np.array(num_comps)
big_comp = np.array(big_comp)
ps = np.array(ps)
plt.figure(1)
plt.loglog(N*ps,(big_comp+0.0)/N,'.')
plt.xlabel('Average degree, k')
plt.ylabel('Size of the largest component/N')
plt.title('Emergence of the giant component')

plt.figure(2)
plt.loglog(N*ps,(num_comps+0.0),'.')
plt.xlabel('Average degree, k')
plt.ylabel('Number of components')
plt.title('Emergence of the totally connected graph')
plt.show()

plt.close(1)
plt.close(2)
