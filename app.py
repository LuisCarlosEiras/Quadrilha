import streamlit as st

# Read the grafo.html file
with open("grafo.html", "r") as f:
  html_data = f.read()

# Display the grafo.html using st.markdown
st.markdown(html_data, unsafe_allow_html=True)
