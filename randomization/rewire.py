import networkx as nx
import random
import copy

def readBiogrid(filename,node_indices=[1,2]):
    
    edges = []

    fi = open(filename,'r')
    for line in fi:
        if line[0]!='#':
            words = line.split('\t')
            if words[12]=='physical':
             edges.append( (words[node_indices[0]], words[node_indices[1]]) )
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

def random_rewired_fast(G, debug=False):
    def order_edge(ed):
        if ed[0]>ed[1]:
            return (ed[1],ed[0])
        else:
            return ed

    ne = G.number_of_edges()
    edge2ind = {}
    ind2edge = {}
    count=0
    for edge in G.edges_iter():
        edge2ind[edge] = count
        ind2edge[count] = edge
        count = count +1
    for i in xrange(10*ne):
        n1 = random.randint(0,ne-1)
        n2 = random.randint(0,ne-1)
        if n1==n2:
            continue
        e1 = ind2edge[n1]
        e2 = ind2edge[n2]
        if random.random()<.5:
            en1 = order_edge((e1[0],e2[1]))
            en2 = order_edge((e1[1],e2[0]))
        else:
            en1 = order_edge((e1[0], e2[0]))
            en2 = order_edge((e1[1], e2[1]))
        # check if new edges already exist
        if (en1 not in edge2ind) and (en2 not in edge2ind):
            # put the new edges in and remove the old edges
            edge2ind.pop(e1)
            edge2ind.pop(e2)
            edge2ind[en1] = n1
            edge2ind[en2] = n2
            
            ind2edge[n1] = en1
            ind2edge[n2] = en2
        else:
            # we had to skip the move
            if debug:
                print "had to skip move"
        if debug:
            if (i%100)==0:
                print "rewired %i times" %i
    Grewired = nx.from_edgelist(edge2ind.keys())
    return Grewired
            
    
    
    
