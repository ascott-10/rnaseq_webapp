import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="RNA-seq Explorer", layout="wide")

st.title("RNA seq navigator")
st.markdown("Upload a .csv  to visualize trend")

st.sidebar.header("Settings")

uploaded_file = st.sidebar.file_uploader("Upload CSV", type = ["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file, index_index=0)

    st.subheader("Data Preview")
    st.write(df.head())

    if st.checkbox("Show summary Preview"):
        st.write(df.describe())
    
    st.subheader("Gene Expression Heatmap")

    top_genes = df.head(20)
    fig, ax = plt.subplots(figsize = (10,5))
    sns.heatmap(top_genes, annot = False, cmap = "YlGnBu", ax= ax)
    st.pyplot(fig)

else:
    st.info("Upload a CSV to begin")