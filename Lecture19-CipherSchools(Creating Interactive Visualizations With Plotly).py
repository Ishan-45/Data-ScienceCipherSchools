# -*- coding: utf-8 -*-
"""Lecture 19 - Creating Interactive Visualizations With Plotly

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1h4YqCTE1yT4nbT-F9hAh7bVD20Bg5ZmB
"""

pip install plotly

import pandas as pd

#load the dataset
df = pd.read_csv('/content/Sales.csv')
print(df.head())

"""Creating a line plot"""

import plotly.express as px

# Load the dataset
fig = px.line(df, x='Memory', y='Storage', title='Sales of mobiles', markers=True)
fig.show()

"""Creating a line plot"""

import plotly.express as px

fig = px.bar(df, x='Memory', y='Storage', title='Sales of mobiles', color='Camera')
fig.show()

"""Creating a Scatter plot"""

import plotly.express as px

fig = px.scatter(df, x='Brands', y='Storage', title='Sales of mobiles', color='Memory', hover_data=['Models'])
fig.show()

"""Creating a Histogram"""

import plotly.express as px

fig = px.histogram(df, x='Brands', y='Selling Price', title='Sales of mobile phones', nbins=10)
fig.show()

"""Creating a Pie chart"""

import plotly.express as px

fig = px.pie(df, values='Selling Price', names='Brands', title='Sales of mobile phones')
fig.show()

# Create an Interactive line chart

fig = px.line(df, x='Brands', y='Storage', title='Sales of mobile phones', markers=True, color='Memory', hover_data=['Storage'])
fig.show()

import plotly.express as px

#Sample data
data = {
    'City' : ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'State' : ['NY','CA','IL','TX','AZ'],
    'Population' : [8419000, 3980400, 2716000, 2328000, 1690000]
}

# Creating the DataFrame
df = pd.DataFrame(data)

# Create a geographical map
fig = px.choropleth(df, locations='State', locationmode='USA-states', color='Population', scope='usa', title='Population by State')
fig.show()
