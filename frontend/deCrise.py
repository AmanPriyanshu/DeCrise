import streamlit as st
import numpy as np
import pandas as pd
import time

st.markdown("""
<style>
.color-font {
    font-size:100px !important;
    color: "red";
}
</style>
""", unsafe_allow_html=True)
st.markdown('<p class="color-font">DeCrise</p>', unsafe_allow_html=True)


st.subheader("Dataset")
data_file = st.file_uploader("Upload CSV", type=['csv'])
if st.button("Process"):
    if data_file is not None:
        # file_details = {"Filename": data_file,
        #                 "FileType": data_file.type, "FileSize": data_file.size}
        # st.write(file_details)

        df = pd.read_csv(data_file)
        st.write(df)
