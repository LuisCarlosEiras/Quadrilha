# https://discuss.streamlit.io/t/unable-to-load-html-file-in-streamlit-app/40186/2

import streamlit as st

# Read the HTML file
with open("grafo.html", "r") as f:
    html_data = f.read()

st.header("Quadrilha")

st.subheader('Using components.v1.html')
st.code('''st.components.v1.html(html_data)''', language='python')
st.components.v1.html(html_data)


