import networkx as nx
import random
def readBiogrid(filename):
    edges = []

    fi = open('BIOGRID-ORGANISM-Arabidopsis_thaliana-3.2.108.tab2.txt','r')
    for line in fi:
        if line[0]!='#':
            words = line.split('\t')
            if words[12]=='physical':
                edges.append( [words[0], words[1]] )
    self_edges = G.selfloop_edges()
    G = nx.from_edgelist(self_edges)
    return G

def numc(H):
    comps = nx.connected_components(H)
    return len(comps)


def rewire_once(H):
    N = H.number_of_edges()
    old_edges = H.edges()
    # 
    n1 = random.randint(0,N-1)
    n2 = random.randint(0,N-1)
    e1 = old_edges[n1]
    e2 = old_edges[n2]
    # try to connect the new edges
    if random.random()>.5:
        enew1 = (e1[0], e2[1])
        enew2 = (e2[0], e1[1])
    else:
        enew1 = (e1[0], e2[0])
        enew2 = (e1[1], e2[1])
    # make sure they don't already exist
    if (not G.has_edge(*enew1))and(not G.has_edge(*enew2)):
        G.a
    
    