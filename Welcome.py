import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write('Hello World')

df = pd.read_csv('Galapagos Islands.csv')
st.dataframe(df)
