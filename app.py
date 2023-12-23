# https://discuss.streamlit.io/t/unable-to-load-html-file-in-streamlit-app/40186/2

# Carrega o arquivo grafo.html
html_file = open("grafo.html", "r").read()

# Exibe o arquivo html
st.markdown(html_file)
