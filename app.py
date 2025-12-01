import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Wine Analysis App", layout="wide")

st.title("🍷 Aplicatie Interactivă – Analiza Vinurilor")

# Upload dataset
uploaded_file = st.file_uploader("Încarcă fișierul de date (.xlsx)", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.success("Fișier încărcat cu succes!")
    
    st.subheader("Primele rânduri din dataset")
    st.write(df.head())

    # Filter
    st.subheader("Filtru interactiv")
    country_list = ["All"] + sorted(df["country"].dropna().unique().tolist())
    selected_country = st.selectbox("Selectează țara", country_list)

    if selected_country != "All":
        df = df[df["country"] == selected_country]

    # Chart 1 — Histogram price
    st.subheader("Distribuția prețurilor")
    plt.figure(figsize=(10,5))
    sns.histplot(df["price"], kde=True)
    st.pyplot(plt.gcf())

    # Chart 2 — Scatter price vs points
    st.subheader("Relația dintre preț și punctaj")
    plt.figure(figsize=(10,5))
    sns.scatterplot(data=df, x="price", y="points", alpha=0.3)
    st.pyplot(plt.gcf())

    # Chart 3 — Boxplot price_per_point per category
    if "price_per_point" in df.columns:
        st.subheader("Distribuția price_per_point pe categorii")
        plt.figure(figsize=(12,6))
        sns.boxplot(data=df, x="category", y="price_per_point")
        st.pyplot(plt.gcf())

else:
    st.info("Încarcă fișierul .xlsx pentru a începe analiza.")
