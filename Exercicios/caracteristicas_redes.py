import networkx as nx
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np


def componentes_conexas(G: nx.Graph):
    if not G.is_directed():
        componentes = list(nx.connected_components(G))
    else:
        componentes = list(nx.weakly_connected_components(G))

    numero_componentes = len(componentes)
    tamanho_maior_componente = 0
    maior_componente = set()

    for comp in componentes:
        if len(comp) > tamanho_maior_componente:
            tamanho_maior_componente = len(comp)
            maior_componente = comp
    
    return componentes, numero_componentes, maior_componente, tamanho_maior_componente


def grau_ponderado_medio(G: nx.Graph):
    return float(sum(dict(G.degree(weight='weight')).values()) / G.number_of_nodes())


def grau_medio(G: nx.Graph):
    return float(sum(dict(G.degree()).values()) / G.number_of_nodes())


def variancia_graus(G:nx.Graph):
    degrees = []
    for _, degree in G.degree():
        degrees.append(degree)
    degrees = np.array(degrees)
    return float(np.var(degrees))


def diametro(G: nx.Graph):
    if nx.is_connected(G):
        return nx.diameter(G)
    
    else:
        maior = max(nx.connected_components(G), key=len)
        subG = G.subgraph(maior)
        return nx.diameter(subG)


def centralidade_grau(G: nx.Graph):
    return nx.degree_centrality(G)


def farness(G: nx.Graph):
    return {n: sum(nx.single_source_shortest_path_length(G, n).values()) for n in G.nodes()}


def closeness(G: nx.Graph):
    return nx.closeness_centrality(G)


def betweenness(G: nx.Graph):
    return nx.betweenness_centrality(G)


def pagerank(G: nx.Graph, alpha=0.85):
    return nx.pagerank(G, alpha=alpha)


def centralidade_autovalor(G: nx.Graph, max_iter=1000):
    return nx.eigenvector_centrality(G, max_iter=max_iter)


def centralidade_katz(G: nx.Graph, alpha=0.1, beta=1.0):
    return nx.katz_centrality(G, alpha=alpha, beta=beta)


def coeficiente_cluster_medio(G: nx.Graph):
    return nx.average_clustering(G)


def distribuicao_graus(G: nx.Graph, loglog=False):
    graus = [deg for _, deg in G.degree()]
    contagem_graus = dict(Counter(graus))
    if loglog:
        plt.loglog(contagem_graus.keys(), contagem_graus.values(), marker="o", linestyle="", color="skyblue", markeredgecolor="black")
        plt.xlabel("Grau (k) [log]")
        plt.ylabel("Número de nós [log]")
        plt.title("Distribuição de graus (log-log)")
    else:
        plt.figure(figsize=(6,4))
        plt.bar(contagem_graus.keys(), contagem_graus.values(), color="skyblue", edgecolor="black")
        plt.xlabel("Grau (k)")
        plt.ylabel("Número de nós")
        plt.title("Distribuição de graus")
    plt.show()
    return contagem_graus