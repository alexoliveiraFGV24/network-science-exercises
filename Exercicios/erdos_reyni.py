import networkx as nx
import matplotlib.pyplot as plt

while True:

    nodes = int(input("Digite o número de nós da rede:"))
    avg_degree = float(input("Digite o grau médio da rede:"))

    p = avg_degree / (nodes - 1)

    N = nx.erdos_renyi_graph(nodes, p, directed=False)
    nx.draw(N, node_color='skyblue', node_size=100)
    plt.show()

    saida = str(input("Aperte q para sair ou qualquer outra tecla para continuar!"))
    if saida == "q":
        break

        