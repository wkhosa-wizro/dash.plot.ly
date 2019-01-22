# coding: utf-8

# this code if from https://dash.plot.ly/getting-started website 

import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7fDBFF'
}


# creating app layout
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(children='Hello Dash', 
           style={'textAlign': 'center',
                 'color': colors['text']
                 }
           ),
    
    html.Div(children='''Dash: A web application framework for Python.''', style={
        'textAlign' : 'center',
        'color' : colors['text']
    }),
    
    dcc.Graph(
        id="example-graph-2",
        figure={
            'data': [
                {'x' : [1, 2, 3], 'y' : [4, 1, 2], 'type' : 'bar', 'name' : 'SF'},
                {'x' : [1, 2, 3], 'y' : [2, 4, 5], 'type' : 'bar', 'name' : u'Montreal'}
            ],
            'layout': {
                'plot_bgcolor' : colors['background'],
                'paper_bgcolor' : colors['background'],
                'font' : {
                    'color' : colors["text"]
                },
                'title': 'Dash Data Visualization'
            }
        })
])

# if running app gives port number in use change port to a different portn no
if __name__ == '__main__':
	app.run_server(debug=True, port='8080')

