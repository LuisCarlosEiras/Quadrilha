import streamlit as st

# Read the HTML file
with open("grafo.html", "r") as f:
    html_data = f.read()

st.header("Deepchecks")

st.write('---')

st.subheader('Using st.markdown')
st.code('''st.markdown(html_data, unsafe_allow_html=True)''', language='python')
st.markdown(html_data, unsafe_allow_html=True)

st.write('---')

st.subheader('Using st.markdown with iframe')
st.code('''st.markdown(f'<iframe srcdoc="{html_data}" width="1000" height="600"></iframe>', unsafe_allow_html=True)''', language='python')
st.markdown(f'<iframe srcdoc="{html_data}" width="1000" height="600"></iframe>', unsafe_allow_html=True)

st.write('---')

st.subheader('Using components.v1.html')
st.code('''st.components.v1.html(html_data)''', language='python')
st.components.v1.html(html_data)
