import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

filename_ls = []
for i in os.listdir():
  if i.endswith('.csv'):
    filename_ls.append(i)

st.write('Hello World!')

df = pd.read_csv('Galapagos Islands.csv')
st.dataframe(df)

options = st.multiselect('select location', filename_ls, filename_ls[0)

el_list = df.columns.tolist()[27:80]
x_axis = st.selectbox('select x-axis element', el_list)
y_axis = st.selectbox('select y-axis element', el_list)

plt.scatter(options[x_axis],options[y_axis])
