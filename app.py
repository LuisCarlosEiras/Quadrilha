import streamlit as st

st.header("Quadrilha, Drummond")
st.subheader('Com o mouse sobre a seta, aparece o verbo')
st.subheader('Apertando o botão do mouse sobre a aresta(círculo), você pode movimentar o grafo') 

# Read the HTML file
with open("grafo.html", "r") as f:
    html_data = f.read()

# Display the grafo.html using st.components.v1.html for full control
st.components.v1.html(html_data, height=800)  # Adjust height as needed
st.components.v1.html(html_data)


