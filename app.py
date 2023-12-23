import streamlit as st

# Read the HTML file
with open("example_page.html", "r") as f:
    html_data = f.read()
    
st.code('''st.components.v1.html(html_data)''', language='python')
st.components.v1.html(html_data)


