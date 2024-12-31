import streamlit as st

st.set_page_config(layout="wide")

pg = st.navigation({
    "Sample": [
        st.Page("pages/sample1.py", title="Sample 1"),
        st.Page("pages/sample2.py", title="Sample 2"),
    ]
})

pg.run()