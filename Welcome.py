import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
from bokeh.plotting import figure

filename_ls = []
for i in os.listdir():
  if i.endswith('.csv'):
    filename_ls.append(i)

st.write('Hello World!')

df = pd.read_csv(i[0])
el_list = df.columns.tolist()[27:80]
# st.dataframe(df)

options = st.multiselect('select location', filename_ls)

x_axis = st.selectbox('select x-axis element', el_list)
y_axis = st.selectbox('select y-axis element', el_list)

# plot with matplotlib (not interctive)
# fig = plt.figure()
# plt.scatter(df[x_axis]/10000, df[y_axis]/10000)
# plt.title('with matplotlib without multiselectbox')
# st.pyplot(fig)

# plot with bokeh
for i in options:
  data = pd.read_csv(i)
  p = figure(x_axis_label=x_axis+' (wt%)', y_axis_label=y_axis+' (wt%)', title=i[:-4])
  p.circle(data[x_axis]/10000, data[y_axis]/10000)
  st.bokeh_chart(p, use_container_width=True)

