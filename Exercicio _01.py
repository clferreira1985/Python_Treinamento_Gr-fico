from turtle import title
import plotly

import plotly.graph_objects as go

fig = go.Figure(
    data=[go.Bar(x=[1,2,3], y=[1,3,2])],
    layout=go.Layout(
        title=go.layout.Title(text='A Figure Specified By A Grph Object')
    )
)
fig.show()

from plotly.subplots import make_subplots

fig = make_subplots(rows=1, cols=2)

fig.add_trace(go.Bar(y=[1,4,5], x=[6,5,2], marker_color="green"), row=1, col=1)
fig.add_trace(go.Scatter(y=[8,2,4,5], x=[6,5,2,7]), row=1, col=2)

fig.update_layout(title_text="Usando O update_layout()", title_font_size=20)

fig.show()

import plotly.graph_objects as go

fig = go.Figure(
    data=[
        go.Bar(x=[1,2,3], y=[1,3,2]),
        go.Scatter(y=[8,3,2], mode="lines")
    ]   
)

fig.update_layout(height=700)
fig.show()

fig = go.Figure(
    data=[
        go.Bar(x=[1,2,3], y=[1,3,2]),
    ]   
)
fig.data[0].marker.line.width=4
fig.data[0].marker.line.color="black"
fig.show()