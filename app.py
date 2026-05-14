import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/cleaned_sales.csv')

st.title("Business Sales Dashboard")

sales_data = df.groupby('Product')['Sales'].sum()

fig, ax = plt.subplots()

sales_data.plot(kind='bar', ax=ax)

st.pyplot(fig)