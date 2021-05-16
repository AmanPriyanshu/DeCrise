import streamlit as st
import numpy as np
import pandas as pd
import time
from test import test
import os

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

st.write(str(os.listdir()))

if st.button("Process"):
    if data_file is not None:
        df = pd.read_csv(data_file)
        df = test(df)
        st.write(df)
