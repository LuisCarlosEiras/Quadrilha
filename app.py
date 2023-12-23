# https://discuss.streamlit.io/t/unable-to-load-html-file-in-streamlit-app/40186/2

import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

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

# Criando a visualização do grafo usando Matplotlib
pos = nx.spring_layout(G)  # Pode ajustar o layout conforme necessário
labels = nx.get_edge_attributes(G, 'action')
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Exibindo a visualização no Streamlit
st.pyplot(plt)



