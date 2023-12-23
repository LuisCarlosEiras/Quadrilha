import streamlit as st
st.header("Quadrilha")
# Read the HTML file
with open("grafo.html", "r") as f:
    html_data = f.read()
# Display the grafo.html using st.components.v1.html for full control
st.components.v1.html(html_data, height=800)  # Adjust height as needed

   
# st.code('''st.markdown(f'<iframe srcdoc="{html_data}" width="1000" height="600"></iframe>', unsafe_allow_html=True)''', language='python')
# st.markdown(f'<iframe srcdoc="{html_data}" width="1000" height="600"></iframe>', unsafe_allow_html=True)

# st.code('''st.components.v1.html(html_data)''', language='python')
st.components.v1.html(html_data)


