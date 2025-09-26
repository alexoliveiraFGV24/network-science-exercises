import networkx as nx
import random
from utils import plot_degree_dist, plot_graph


def erdos_reyni_aleatorio(N:int, grau_medio:float):
    p = grau_medio / (N - 1)
    G = nx.erdos_renyi_graph(N, p, directed=False)
    return G


def anexacao_uniforme(N:int, momentos:int) -> nx.Graph:
    nos = list(range(1, N+1))
    G = nx.Graph()
    G.add_nodes_from(nos)
    for no in nos:
        nos_ligantes_possiveis = [n for n in nos if n != no]
        escolhidos = random.sample(nos_ligantes_possiveis, min(momentos, N-1))
        for no_ligante in escolhidos:
            G.add_edge(no, no_ligante)
    return G


def price_model(N:int, p:float) -> nx.Graph:
    pass