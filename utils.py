import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter


def plot_degree_dist(G: nx.Graph, loglog:bool=False) -> None:
    degrees = [deg for _, deg in G.degree()]
    degree_count = dict(Counter(degrees))
    if loglog:
        plt.loglog(degree_count.keys(), degree_count.values(), marker="o", linestyle="", color="skyblue", markeredgecolor="black")
        plt.xlabel("Grau (k) [log]")
        plt.ylabel("Número de nós [log]")
        plt.title("Distribuição de graus (log-log)")
    else:
        plt.figure(figsize=(6,4))
        plt.bar(degree_count.keys(), degree_count.values(), color="skyblue", edgecolor="black")
        plt.xlabel("Grau (k)")
        plt.ylabel("Número de nós")
        plt.title("Distribuição de graus")
    plt.show()


def plot_graph(G:nx.Graph) -> None:
    nx.draw(G, node_color='skyblue', node_size=100)
    plt.show()