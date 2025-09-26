import networkx as nx
import random


"""
Funções prontas do networkx

nx.watts_strogatz_graph(n, k, p)
nx.powerlaw_cluster_graph(n, m, p)
nx.erdos_renyi_graph(n, p)
nx.barabasi_albert_graph(n, m)
"""


def erdos_reyni_aleatorio(N:int, grau_medio:float, G:nx.graph=None):
    if not G:
        G = nx.Graph()

    nos_antigos_G = list(nx.nodes(G))
    nos_adicionais = list(range(len(nos_antigos_G) + 1, len(nos_antigos_G) + N + 1))
    G.add_nodes_from(nos_adicionais)
    p = grau_medio / (len(nos_antigos_G) + N - 1)

    for no_adicional in nos_adicionais:
        nos_ligantes_possiveis = [n for n in nos_adicionais if n != no_adicional] + nos_antigos_G
        for no_ligante in nos_ligantes_possiveis:
            if random.random() < p:
                G.add_edge(no_adicional, no_ligante)

    return G


def anexacao_uniforme(N:int, m:int, G:nx.graph=None) -> nx.Graph:
    if not G:
        G = nx.Graph()
    
    nos_antigos_G = list(nx.nodes(G))
    nos_adicionais = list(range(len(nos_antigos_G) + 1, len(nos_antigos_G) + N + 1))
    G.add_nodes_from(nos_adicionais)

    for no_adicional in nos_adicionais:
        nos_ligantes_possiveis = [n for n in nos_adicionais if n != no_adicional] + nos_antigos_G
        escolhidos = random.sample(nos_ligantes_possiveis, min(m, N-1))
        for no_ligante in escolhidos:
            G.add_edge(no_adicional, no_ligante)

    return G


def anexacao_preferencial(N:int, m:int, G:nx.graph=None) -> nx.Graph:
    if not G:
        G = nx.Graph()
    
    nos_antigos_G = list(nx.nodes(G))
    nos_adicionais = list(range(len(nos_antigos_G) + 1, len(nos_antigos_G) + N + 1))
    G.add_nodes_from(nos_adicionais)

    lista_graus = []
    for no, grau in G.degree():
        lista_graus.extend([no]*grau)

    for novo_no in nos_adicionais:
        nos_existentes = set()
        while len(nos_existentes) < min(m, len(lista_graus)):
            escolhido = random.choice(lista_graus)
            nos_existentes.add(escolhido)
        for no in nos_existentes:
            G.add_edge(novo_no, no)
        lista_graus.extend(list(nos_existentes))
        lista_graus.extend([novo_no]*len(nos_existentes))

    return G


def modelo_price(G: nx.DiGraph = None, N: int = 1, m: int = 1, k0: float = 1.0) -> nx.DiGraph:
    if G is None:
        G = nx.DiGraph()

    nos_antigos_G = list(G.nodes())
    nos_adicionais = list(range(len(nos_antigos_G) + 1, len(nos_antigos_G) + N + 1))
    G.add_nodes_from(nos_adicionais)

    lista_graus = []
    for no in G.nodes():
        grau_entrada = G.in_degree(no)
        multiplicidade = int(grau_entrada + k0)
        lista_graus.extend([no]*multiplicidade)

    for novo_no in nos_adicionais:
        nos_existentes = set()
        while len(nos_existentes) < min(m, len(lista_graus)):
            escolhido = random.choice(lista_graus)
            nos_existentes.add(escolhido)
        for no in nos_existentes:
            G.add_edge(novo_no, no)
        for no in nos_existentes:
            lista_graus.append(no) 
        lista_graus.extend([novo_no]*m)

    return G


def bianconi_barabasi(N:int, m:int, m0:int = 3) -> nx.Graph:
    G = nx.complete_graph(m0)
    fitness = {i: random.random() for i in G.nodes()}

    for novo_no in range(m0, N):
        G.add_node(novo_no)
        fitness[novo_no] = random.random()
        probs = []
        nos_existentes = list(G.nodes())
        nos_existentes.remove(novo_no)
        soma = sum(fitness[n]*G.degree(n) for n in nos_existentes)
        for n in nos_existentes:
            prob = (fitness[n] * G.degree(n)) / soma if soma > 0 else 0
            probs.append(prob)
        escolhidos = set()
        while len(escolhidos) < m:
            escolhido = random.choices(nos_existentes, weights=probs, k=1)[0]
            escolhidos.add(escolhido)
        for n in escolhidos:
            G.add_edge(novo_no, n)

    return G