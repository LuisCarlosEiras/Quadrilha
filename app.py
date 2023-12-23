import warnings
warnings.filterwarnings("ignore")

from pyvis.network import Network
import networkx as nx

# Criação do grafo direcionado
G = nx.DiGraph()

# Adicionando as arestas ao grafo
G.add_edge("João", "Teresa", action="amava")
G.add_edge("Teresa", "Raimundo", action="amava")
G.add_edge("Raimundo", "Maria", action="amava")
G.add_edge("Maria", "Joaquim", action="amava")
G.add_edge("Joaquim", "Lili", action="amava")
G.add_edge("Lili", "ninguém", action="amava")
G.add_edge("João", "Estados Unidos", action="foi pra")
G.add_edge("Teresa", "convento", action="foi para")
G.add_edge("Raimundo", "desastre", action="morreu de")
G.add_edge("Maria", "tia", action="ficou para")
G.add_edge("Joaquim", "suicídio", action="cometeu")
G.add_edge("Lili", "J. Pinto Fernandes", action="casou com")
G.add_edge("J. Pinto Fernandes", "história", action="que não tinha entrado na")
G.add_edge("Quadrilha","Drummond", action="autor")

# Criação do grafo interativo
net = Network(notebook=True)
net.from_nx(G)

# Configuração das arestas para mostrar a ação quando o mouse passa por cima
for edge in net.edges:
    edge['title'] = edge['action']
    edge['arrows'] = 'to' # Adicionando seta nas arestas
# cdn_resources='in_line'
# Mostrando o grafo
net.show("grafo.html")
