#importing packages
import plotly.graph_objects as go
import pandas as pd
import numpy as np

#dataframe declarations
df = pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())
df2 = pd.DataFrame({'Category':['A','B','C'],'Values':[32,43,50]})
df3 = pd.DataFrame({'x':[1,2,3,4,5],'y':[10,20,30,20,10],'z':[5,4,3,2,1]})

#creating a scatter plot between A and B
fig = go.Figure(
                data=[go.Scatter(x=df['A'],y=df['B'],mode='markers',marker_size=10)],
                layout_title_text="Scatter Plot"
)
fig.show()

#creating a bar plot between Category and Values
fig = go.Figure(
                data=[go.Bar(x=df2['Category'],y=df2['Values'])],
                layout_title_text="Bar Plot"
)
fig.show()






