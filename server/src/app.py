# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import os
from dash.dependencies import Input, Output
import dash_table

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('./server/src/assets/13TOKYO.csv')


app.layout = html.Div(children=[
    html.H1(children='Dash Sample'),

    html.A('repos', href='https://github.com/tettasun/dash-sample', target="_blank"),
    html.Div(children='''
        dash testing site
    '''),
    html.H4(children='Image'),
    html.Img(src=app.get_asset_url('tokyo.png')),

    html.Label('Dropdown'),
    dcc.Dropdown(
        id='region-dropdown',
        options=[
            {'label': u'千代田区', 'value': 'CHIYODA'},
            {'label': '新宿区', 'value': 'SHINJUKU'},
        ],
        value='CHIYODA'
    ),

    html.H4(children='test result'),
    dash_table.DataTable(
        id='table',
        columns=[ {"name": i, "id": i} for i in df.columns],
        data=df.to_dict("rows")
    ),

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

# callbacks
# @app.callback(
#     Output('output-container', 'children'),
#     [Input('region-dropdown', 'value')])
# def input_triggers_spinner(value):
#     time.sleep(2)
#     return html.Img(src=value, height="30%", width="30%", style={"margin": "10%"})




if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)
