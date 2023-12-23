# https://discuss.streamlit.io/t/unable-to-load-html-file-in-streamlit-app/40186/2

import streamlit as st
from pyvis.network import Network
import networkx as nx
import os

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
G.add_edge("Quadrilha", "Drummond", action="autor")

# Criação do grafo interativo
net = Network(notebook=False)
net.from_nx(G)

# Configuração das arestas para mostrar a ação quando o mouse passa por cima
for edge in net.edges:
    edge['title'] = edge['action']
    edge['arrows'] = 'to'  # Adicionando seta nas arestas

# Salvar o grafo como um arquivo HTML temporário
temp_html_file = "temp_graph.html"
net.show(temp_html_file)

# Exibir o grafo HTML no Streamlit
with open(temp_html_file, "r", encoding="utf-8") as f:
    st.components.v1.html(f.read(), width=800, height=600)

# Remover o arquivo temporário
os.remove(temp_html_file)
