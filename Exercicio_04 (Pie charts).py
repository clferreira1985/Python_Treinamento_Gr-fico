 import plotly.graph_objects as go

labels = ['Oxigênio', 'Higrogênio', 'Gás Carbônio', 'Nitrogênio']
values = [4500,2500,1053,500]

fig = go.Figure(data=go.Pie(labels=labels, values=values))
fig.update_traces(hoverinfo='label+percent', textinfo='value+percent', textfont_size=15,
marker=dict(colors=['green','blue','yellow','grey']))
fig.show()


fig = go.Figure(data=go.Pie(labels=labels, values=values, pull = [0, 0, 0.2, 0]))
fig.update_traces(hoverinfo='label+percent', textinfo='value+percent', textfont_size=15,
marker=dict(colors=['green','blue','yellow','grey']))
fig.show()
