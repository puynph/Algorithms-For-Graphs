#! /usr/bin/env python

"""
This file of code implements Ford-Fulkerson to find the
"""
from graafi3 import Graph
from copy import deepcopy as copy


# Read a set containing vertices.
def ReadNodes(filename):
    ff = open(filename, 'r')
    x = ff.readlines()[0].split()
    S = []
    for i in x:
        S.append(int(i))
    return S


# Add the flows in f1 and f2.
def SumFlow(f1, f2):
    f = copy(f1)
    for (u, v) in f2:
        if not (u, v) in f:
            f[(u, v)] = f2[(u, v)]
        else:
            f[(u, v)] += f2[(u, v)]
    return f


# Form the residual network.
def MakeResidual(G, f):
    Gr = copy(G)
    for (u, v) in f:
        c = 0
        # Copy the weight
        if (u, v) in Gr.W:
            c = Gr.W[(u, v)]
        # calculate residual capacity
        cf = c - f[(u, v)]
        if not v in Gr.AL[u]:
            Gr.addEdge(u, v)
        Gr.W[(u, v)] = cf
    return Gr


# This function is not complete. You must provide code to make it work properly.
def FindAugPath(Gr, s, t):
    """
    :param: Graph, source, sink
    :return: augmented path

    This function finds a path from source to sink using BFS. A path is formed only if each edge's weight
    in the path is greater than 0.
    """
    aug = []
    # laskuri is a counter to see how many edges are processed in total
    laskuri = 0
    queue = [s]
    parents = {s: None}
    visited = [s]

    while len(queue) != 0:
        u = queue.pop(0)
        for v in Gr.adj(u):
            laskuri += 1
            if v not in visited and Gr.W[(u, v)] > 0:
                parents[v] = u
                queue.append(v)
                visited.append(v)

            # When the vertex has reached the sink, it is then appended to the path
            # from the sink, backtrack the path to its parents (the parents dict was set using BFS)
            if v == t and Gr.W[(u, v)] > 0:
                aug.append(t)
                p = parents[t]
                aug.append(p)  # append source since the while loop does not include this
                # backtrack to the node's parent until we reach the source
                while p != s:
                    p = parents[p]
                    aug.append(p)
                aug.reverse()
                # print(aug)
                return aug, laskuri

    # return an empty list in case there is no path from source to sink
    return aug, laskuri


def MakeAugFlow(Gr, s, t, path):
    """
    :param: Graph, source, sink, augmented path
    :return: a dictionary - key : (u,v)/ payload : flow magnitude

    This function check the validation of the returned path from FindAugPath function.
    It finds the minimum capacity from different edges and therefore make the flow possible for the path
    """
    f = {}
    if not path:
        return f
    if path[0] != s:
        raise Exception("Path not from s")
    if path[-1] != t:
        raise Exception("Path not to t")

    """ 
    cfp is the minimum capacity
    This variable is initially assigned to the value of the capacity of the first edge found in path.
    It is then compared with other edges until the end of the path. A minimum value is found.
    """
    # You may want to see different possible path and cfp from each iteration
    # print(path)
    cfp = Gr.W[(path[0], path[1])]
    for i in range(1, len(path)):
        cfp = min(Gr.W[(path[i - 1], path[i])], cfp)
    # print(cfp)

    """
    cfp is applied to every arc in the path, fulfill the capacity constraint 
    and the anti-symmetry property
    """
    for i in range(1, len(path)):
        f[(path[i - 1], path[i])] = cfp
        f[(path[i], path[i-1])] = -cfp

    # print(f)
    return f


def FordFulkerson(G, s, t):
    # laskuri is a counter to see how many edges are processed in total
    laskuri = 0
    f = {}
    pp = FindAugPath(G, s, t)
    p = pp[0]
    laskuri += pp[1]
    fp = MakeAugFlow(G, s, t, p)
    f = SumFlow(f, fp)
    Gr = MakeResidual(G, f)
    i = 0
    while p and i < 1000:
        # signal of different loop
        # print("ss")
        i += 1
        pp = FindAugPath(Gr, s, t)
        p = pp[0]
        laskuri += pp[1]
        fp = MakeAugFlow(Gr, s, t, p)
        f = SumFlow(f, fp)
        Gr = MakeResidual(G, f)

    """
    Calculate the flow magnitude: the magnitude is the amount of flow leaving the source vertex.
    """
    flow_mag = 0
    for (u, v) in f:
        if u == 1:
            flow_mag += f[(u, v)]

    print("Laskuri laski: " + str(laskuri))
    print("Flow magnitude: ", flow_mag)
    return f


G = Graph("testflow_10000")
S = ReadNodes("testset_10000")
s = S[0]
t = S[1]

print(FordFulkerson(G, s, t))
