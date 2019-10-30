# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import os
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('./server/src/assets/13TOKYO.csv')

print('df', df)

def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

app.layout = html.Div(children=[
    html.H1(children='Dash Sample'),

    html.Div(children='''
        Hoge
    '''),
    html.H4(children='Image'),
    html.Img(src=app.get_asset_url('tokyo.png')),

    html.Label('Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': '失敗', 'value': 'FAIL'},
            {'label': u'成功', 'value': 'SUCCES'},
        ],
        value='SUCCES'
    ),

    html.H4(children='test result'),
    generate_table(df, 48),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),

])



if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)
