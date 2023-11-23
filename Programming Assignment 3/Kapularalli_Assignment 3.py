#! /usr/bin/env python
""" Monte carlo simulator for Kapularalli game """
""" the "Jump probability" is fixed at 0.001, or 1/1000 """

from graafi3 import Graph
import random

""" Playing Pelaa(g,n) plays n rounds using g """
""" Pagerank Algorithm can be utilized to produce the probability that the baton can be passed to any player"""

def Pagerank(g, d):
    """
    This function calculates the probability for each node's chances of 'getting the baton'
    using Pagerank. Pagerank is calculated as the given formula in course note.
    For weighted graph, there is an additional step taking place after Pagerank for each node
    is calculated. There is another possibility of the node passing the baton to one of its adjacent
    depending on the edge's weight.
    In this case, the Pagerank value is multiplied by the 'weight possibility' (formula given in the assignment)
    because these two are independent probabilities P(A and B) = P(A)*P(B)
    """
    Nodes = [u for u in g.V]
    # create a dictionary: key-nodes, payload-Page rank value
    Pagerank = {u: 1/len(Nodes) for u in g.V}
    i = 0
    while i < 100:
        # a new dictionary is created for each iteration to calculate
        # different node's Pagerank
        new_page_rank = {}
        i += 1
        for u in Nodes:
            # print("Current node:", u)
            total_prob_adj = 0
            for node in Nodes:
                # node is the parent of u
                if u in g.adj(node):
                    total_prob_adj += Pagerank[node]/len(g.adj(node))
            # Pagerank of u is calculated by summing up the ration of its p[u] Pagerank over out-degree of p[u]
            new_page_rank[u] = total_prob_adj
        # update Pagerank value
        Pagerank = new_page_rank

    # consider damping factor d
    for u in Pagerank:
        Pagerank[u] = d / len(Nodes) + (1-d) * Pagerank[u]

    if bool(g.W):
        for u in Nodes:
            # print("Current node:", u)
            total_prob_weight = 0
            for node in Nodes:
                if u in g.adj(node):
                    total_node_weight = 0
                    for adj_node in g.adj(node):
                        total_node_weight += g.W[node, adj_node]
                    # print("Node:",node, "Weight:",g.W[(node,u)])
                    # print(g.W[(node, u)]/total_node_weight)
                    total_prob_weight += g.W[(node, u)]/total_node_weight
            Pagerank[u] *= total_prob_weight

    return [u[0] for u in sorted(Pagerank.items(), key=lambda x: x[1], reverse=True)]

def Pelaa(g, n):
    """This template may not consider the weighted graph """
    random.seed(6)
    d = 0.01
    Nodes = [u for u in g.V]
    Points = {u:0 for u in g.V}
    i = 0
    while i < n:
        i += 1
        j = 0
        u = Nodes[int(random.random()*len(Nodes))]
        k = 2*len(Nodes)
        while j < k:
            j += 1
            if random.random() <= d:
                u = Nodes[int(random.random()*len(Nodes))]
                continue
            A = g.adj(u)
            u = A[int(random.random()*len(A))]
        Points[u] += 1
    return [u[0] for u in sorted(Points.items(), key = lambda x: x[1], reverse = True)]


if __name__ == "__main__":
    g = Graph('walk_random_101_512')
    u = Pagerank(g, 0.01)
    print("Pagerank:", u)
    b = Pelaa(g, 10000)
    print("Monte Carlo:", b)
