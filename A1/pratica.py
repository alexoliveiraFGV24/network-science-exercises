import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import os

"""
Exiba um grafo com não mais do que 20 nós, onde o nó com maior grau não é o nó com 
maior centralidade por PageRank.
"""
def plot_graph(G:nx.Graph) -> None:
    nx.draw(G, node_color='skyblue', node_size=100)
    plt.show()
def pagerank(G: nx.Graph, alpha=0.85):
    return nx.pagerank(G, alpha=alpha)
def centralidade_grau(G: nx.Graph):
    return nx.degree_centrality(G)

# Grafo direcionado em que muitos links saem de 1, mas pouco retornam
# G = nx.DiGraph()
# G.add_edges_from([
#     (1,2),(1,3),(1,4),(1,5),
#     (4,6),(6,3),(3,7),(7,2)    
# ])
# plot_graph(G)
# pr = nx.pagerank(G)
# cg = nx.degree_centrality(G)
# print("Nó com maior PageRank:", max(pr.items(), key=lambda x: x[1]))
# print("Nó com maior centralidade de grau:", max(cg.items(), key=lambda x: x[1]))



"""
Para cada rede calcule: 
1) O número de componentes conexas. 
2) O tamanho relativo da maior componente conexa. 
3) O grau médio. 
4) A variância dos graus. 
5) A distribuição dos graus.
"""
def DATA_FOLDER():
    return os.path.join(os.getcwd(), "A1", "data")

rede1 = pd.read_csv(os.path.join(DATA_FOLDER(), "rede1.csv"))
rede2 = pd.read_csv(os.path.join(DATA_FOLDER(), "rede2.csv"))
rede1 = rede1.to_numpy()
rede2 = rede2.to_numpy()

G1 = nx.Graph()
G2 = nx.Graph()

for aresta in rede1:
    G1.add_edge(aresta[0], aresta[1])
for aresta in rede2:
    G2.add_edge(aresta[0], aresta[1])