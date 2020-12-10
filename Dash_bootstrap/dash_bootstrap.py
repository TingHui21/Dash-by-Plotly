import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pandas_datareader.data as web
import datetime

# start = datetime.datetime(2020, 1, 1)
# end = datetime.datetime(2020, 12, 3)

# df = web.DataReader(['AMZN', 'GOOGL', "FB", "PFE"],
#                     "stooq", start=start, end=end)

# df = df.stack().reset_index()

# df.to_csv("stocks.csv", index=False)

df = pd.read_csv("stocks.csv")

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{"name": "viewport",
                            "content": "width=device-width, initial-scale=1.0"}])

# Layout
# ------------------------------------

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Stock Market Dashboard",
                        className='text-primary text-center , mb-4'), width=12)
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Dropdown(id="my-dpdn", multi=False, value="AMZN",
                         options=[{'label': x, "value": x}
                                  for x in sorted(df['Symbols'].unique())]),
            dcc.Graph(id='line-fig')], width={'size': 5, "offset": 1, 'order': 1}),
        dbc.Col([
            dcc.Dropdown(id='my-dpdn2', multi=True, value=['PFE', 'FB'],
                         options=[{'label': x, 'value': x}
                                  for x in sorted(df['Symbols'].unique())]),
            dcc.Graph(id='line-fig2')], width={'size': 5, 'order': 2})

    ]),

    dbc.Row([

    ]),



], fluid=True)

if __name__ == "__main__":
    app.run_server(debug=True)
