import streamlit as st
import pandas as pd

df = pd.read_excel('sample.xlsx')

st.title('Excel Table')
edited_df = st.data_editor(df, num_rows="dynamic")

if st.button('Save Changes'):
    # edited_df.to_excel('your_excel_file_updated.xlsx', index=False)
    st.success('Changes saved successfully!')