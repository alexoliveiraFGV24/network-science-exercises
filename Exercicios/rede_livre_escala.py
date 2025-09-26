import networkx as nx
import numpy as np
import random

"""
Funções no networkx

nx.barabasi_albert_graph(n, m)
nx.powerlaw_cluster_graph(n, m, p)
nx.scale_free_graph(n)
"""


def rede_livre_escala(N:int, gamma:float, k_min):
    G = nx.Graph()
    G.add_nodes_from(range(1, N+1))

    r = np.random.random(N)
    k = np.floor(k_min * (1 - r) ** (-1/(gamma - 1))).astype(int)

    if sum(k) % 2 != 0:
        k[0] += 1

    stub_list = []
    for i, deg in enumerate(k):
        stub_list.extend([i]*deg)
    
    random.shuffle(stub_list)

    while len(stub_list) > 1:
        a = stub_list.pop()
        b = stub_list.pop()
        if a != b:
            G.add_edge(a, b)
        else:
            stub_list.extend([a, b])
            random.shuffle(stub_list)
    
    return G