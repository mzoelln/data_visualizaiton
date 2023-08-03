import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

filename_ls = []
for i in os.listdir():
  if i.endswith('.csv'):
    filename_ls.append(i)

st.write(filename_ls)

st.write('Hello World!')

df = pd.read_csv('Galapagos Islands.csv')
st.dataframe(df)

el_list = df.columns.tolist()[27:80]
x_axis = st.selectbox('select element', el_list)
