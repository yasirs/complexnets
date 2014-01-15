import networkx as nx
import random
import copy

def readBiogrid(filename):
    edges = []

    fi = open(filename,'r')
    for line in fi:
        if line[0]!='#':
            words = line.split('\t')
            if words[12]=='physical':
                edges.append( [words[0], words[1]] )
    G = nx.from_edgelist(edges)
    self_edges = G.selfloop_edges()
    G.remove_edges_from(self_edges)
    return G

def numc(H):
    comps = nx.connected_components(H)
    return len(comps)


def rewire_once(H, debug=False):
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
    if (not H.has_edge(*enew1))and(not H.has_edge(*enew2)):
        H.add_edges_from([enew1, enew2])
        H.remove_edges_from([e1,e2])
        if debug:
            print "removed ", [e1,e2]
            print "added ", [enew1, enew2]


def random_rewired(G, debug=False):
    Gcopy = copy.deepcopy(G)
    # get number of edges
    ne = Gcopy.number_of_edges()
    for i in xrange(2*ne):
        rewire_once(Gcopy)
        if debug:
            if (i%100)==0:
                print "done %i rewires" %i
    return Gcopy
    
    
    
    