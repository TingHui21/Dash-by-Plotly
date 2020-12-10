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
            dcc.Graph(id='line-fig')],  # width={'size': 5, "offset": 1, 'order': 1}
            xs=12, sm=12, md=12, lg=5, xl=5

        ),
        dbc.Col([
            dcc.Dropdown(id='my-dpdn2', multi=True, value=['PFE', 'FB'],
                         options=[{'label': x, 'value': x}
                                  for x in sorted(df['Symbols'].unique())]),
            dcc.Graph(id='line-fig2')],  # width={'size': 5, 'order': 2}
            xs=12, sm=12, md=12, lg=5, xl=5
        )

    ]),

    dbc.Row([
        dbc.Col([
            html.P('Select Company Stock:',
                   style={'textDecoration': 'underline'}),
            dcc.Checklist(id='my-checklist', value=['FB', 'GOOGL', 'AMZN'],
                          options=[{'label': x, "value": x}
                                   for x in sorted(df['Symbols'].unique())],
                          labelClassName='mr-3'),
            dcc.Graph(id='my-hist')
        ], width={'size': 5, 'offset': 1}),

        dbc.Col([
            dbc.Card([
                dbc.CardBody(
                    html.P("We are better together,help each other out",
                           className='card-text')
                ),
                dbc.CardImg(
                    src="https://media3.giphy.com/media/sqdHf81hmZHQA/giphy.gif?cid=ecf05e47d6vb4x2vmgk59s0iwwuwerf69taxy9lpix69tjfs&rid=giphy.gif",
                    bottom=True),
            ], style={"width": "20rem"})
        ], width={'size': 3, "offset": 1})
    ], align='center'),
], fluid=True)

# Line chart - Single


@app.callback(
    Output('line-fig', "figure"),
    Input('my-dpdn', 'value')
)
def update_graph(stock_slctd):
    dff = df[df['Symbols'] == stock_slctd]
    figIn = px.line(dff, x='Date', y='High')
    return figIn


@app.callback(
    Output('line-fig2', 'figure'),
    Input('my-dpdn2', 'value')
)
def update_graph2(stocks_slctd):
    dff = df[df['Symbols'].isin(stocks_slctd)]
    figIn2 = px.line(dff, x='Date', y='High', color='Symbols')
    return figIn2


@app.callback(
    Output("my-hist", 'figure'),
    Input('my-checklist', 'value')
)
def update_graph3(stocks_slctd):
    dff = df[df['Symbols'].isin(stocks_slctd)]
    dff = dff[dff['Date'] == '2020-12-03']
    figIn3 = px.histogram(dff, x='Symbols', y='Close')
    return figIn3


if __name__ == "__main__":
    app.run_server(debug=True)

# Line chart - Multiple
