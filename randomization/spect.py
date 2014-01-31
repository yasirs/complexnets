import networkx as nx
import numpy as np
import scipy.linalg
import pylab

def neighborhood_modularity(G):
	nm = {}
	for node in G:
		nb = G.neighbors(node)
		A = nx.to_numpy_matrix(G.subgraph(nb))
		if np.sum(A)>0:
			D = sum(A)
			B = A - np.multiply(D,D)/np.sum(A)
			eigs = sorted(scipy.linalg.eigvals(B))
			nm[node] = (eigs[-1].real, eigs[0].real)
	return nm

def deg_nm(G):
	nm = neighborhood_modularity(G)
	cl = nx.clustering(G)
	d = []
	for n in G:
		if n in nm:
			d.append([G.degree(n),cl[n],nm[n][0],nm[n][1],max(np.abs(nm[n]))])
		else:
			d.append([G.degree(n),cl[n],0,0,0])
	d = np.array(d)
	return d

