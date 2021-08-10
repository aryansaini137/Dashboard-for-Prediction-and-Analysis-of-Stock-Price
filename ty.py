import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import numpy as np


app = dash.Dash()
server = app.server

df= pd.read_csv("stock_data.csv")
app.layout = html.Div([

            dcc.Tab(label='Facebook Stock Data', children=[
                html.Div([
                    html.H1("Stocks High vs Lows",
                            style={'textAlign': 'center'}),

                    dcc.Dropdown(id='my-dropdown',
                                 options=[{'label': 'Tesla', 'value': 'TSLA'},
                                          {'label': 'Apple','value': 'AAPL'},
                                          {'label': 'Facebook', 'value': 'FB'},
                                          {'label': 'Microsoft','value': 'MSFT'}],
                                 multi=True,value=['FB'],
                                 style={"display": "block", "margin-left": "auto",
                                        "margin-right": "auto", "width": "60%"}),
                    dcc.Graph(id='highlow'),
                    html.H1("Stocks Market Volume", style={'textAlign': 'center'}),

                    dcc.Dropdown(id='my-dropdown2',
                                 options=[{'label': 'Tesla', 'value': 'TSLA'},
                                          {'label': 'Apple','value': 'AAPL'},
                                          {'label': 'Facebook', 'value': 'FB'},
                                          {'label': 'Microsoft','value': 'MSFT'}],
                                 multi=True,value=['FB'],
                                 style={"display": "block", "margin-left": "auto",
                                        "margin-right": "auto", "width": "60%"}),
                    dcc.Graph(id='volume')
                ], className="container"),
            ])


            ])







@app.callback(Output('highlow', 'figure'),
      [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown):
    dropdown = {"TSLA": "Tesla","AAPL": "Apple","FB": "Facebook","MSFT": "Microsoft",}
    trace1 = []
    trace2 = []
    for stock in selected_dropdown:
        trace1.append(
          go.Scatter(x=df[df["Stock"] == stock]["Date"],
                     y=df[df["Stock"] == stock]["High"],
                     mode='lines', opacity=0.7,
                     name=f'High {dropdown[stock]}',textposition='bottom center'))
        trace2.append(
          go.Scatter(x=df[df["Stock"] == stock]["Date"],
                     y=df[df["Stock"] == stock]["Low"],
                     mode='lines', opacity=0.6,
                     name=f'Low {dropdown[stock]}',textposition='bottom center'))
    traces = [trace1, trace2]
    data = [val for sublist in traces for val in sublist]
    figure = {'data': data,
          'layout': go.Layout(colorway=["#5E0DAC", '#FF4F00', '#375CB1',
                                        '#FF7400', '#FFF400', '#FF0056'],
        height=600,
        title=f"High and Low Prices for {', '.join(str(dropdown[i]) for i in selected_dropdown)} Over Time",
        xaxis={"title":"Date",
               'rangeselector': {'buttons': list([{'count': 1, 'label': '1M',
                                                   'step': 'month',
                                                   'stepmode': 'backward'},
                                                  {'count': 6, 'label': '6M',
                                                   'step': 'month',
                                                   'stepmode': 'backward'},
                                                  {'step': 'all'}])},
               'rangeslider': {'visible': True}, 'type': 'date'},
         yaxis={"title":"Price (USD)"})}
    return figure


@app.callback(Output('volume', 'figure'),
      [Input('my-dropdown2', 'value')])
def update_graph(selected_dropdown_value):
    dropdown = {"TSLA": "Tesla","AAPL": "Apple","FB": "Facebook","MSFT": "Microsoft",}
    trace1 = []
    for stock in selected_dropdown_value:
        trace1.append(
          go.Scatter(x=df[df["Stock"] == stock]["Date"],
                     y=df[df["Stock"] == stock]["Volume"],
                     mode='lines', opacity=0.7,
                     name=f'Volume {dropdown[stock]}', textposition='bottom center'))
    traces = [trace1]
    data = [val for sublist in traces for val in sublist]
    figure = {'data': data,
          'layout': go.Layout(colorway=["#5E0DAC", '#FF4F00', '#375CB1',
                                        '#FF7400', '#FFF400', '#FF0056'],
        height=600,
        title=f"Market Volume for {', '.join(str(dropdown[i]) for i in selected_dropdown_value)} Over Time",
        xaxis={"title":"Date",
               'rangeselector': {'buttons': list([{'count': 1, 'label': '1M',
                                                   'step': 'month',
                                                   'stepmode': 'backward'},
                                                  {'count': 6, 'label': '6M',
                                                   'step': 'month',
                                                   'stepmode': 'backward'},
                                                  {'step': 'all'}])},
               'rangeslider': {'visible': True}, 'type': 'date'},
         yaxis={"title":"Transactions Volume"})}
    return figure



if __name__=='__main__':
    app.run_server(debug=True)
