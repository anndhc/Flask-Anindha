from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H3("Dashboard Data Dunia"),
    dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id='radio'),
    dcc.Graph(id='graph')
])

@callback(
    Output('graph', 'figure'),
    Input('radio', 'value')
)
def update_graph(col):
    fig = px.histogram(df, x='continent', y=col, histfunc='avg')
    return fig

if __name__ == '__main__':
    app.run(debug=True)
