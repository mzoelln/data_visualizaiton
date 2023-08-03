import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
from bokeh.plotting import figure, show
from bokeh.io import output_notebook

filename_ls = []
for i in os.listdir():
  if i.endswith('.csv'):
    filename_ls.append(i)

st.write('Hello World!')

df = pd.read_csv('Galapagos Islands.csv')
st.dataframe(df)

options = st.multiselect('select location', filename_ls)

el_list = df.columns.tolist()[27:80]
x_axis = st.selectbox('select x-axis element', el_list)
y_axis = st.selectbox('select y-axis element', el_list)

fig = plt.figure()
plt.scatter(df[x_axis], df[y_axis])
st.pyplot(fig)

output_notebook()
p = figure(x_axis_label=x_axis+' (wt%)', y_axis_label=y_axis+' (wt%)')
p.circle(df[x_axis]/10000, df[y_axis]/10000)
show(p)

st.bokeh_chart(p, use_container_width=True)
