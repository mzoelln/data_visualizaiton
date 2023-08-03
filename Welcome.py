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

st.write('Plotting data with bokeh in Streamlit')

df = pd.read_csv(filename_ls[0])
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
  p.line([data[x_axis].min()/10000, data[x_axis].max()/10000], [data[y_axis].mean()/10000,data[y_axis].mean()/10000], line_color='green' )
  p.rect(x=df['x_axis'].mean()/10000, y=df['y_axis'].mean()/10000, width=df['x_axis'].std()/10000, height=df['y_axis'].std()/10000, color='blue', fill_alpha=0.5)
  p.line([data[x_axis].mean()/10000, data[x_axis].mean()/10000], [data[y_axis].min()/10000,data[y_axis].max()/10000], line_color='red' )
  st.bokeh_chart(p, use_container_width=True)

