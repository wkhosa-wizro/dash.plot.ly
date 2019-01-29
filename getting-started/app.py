# coding: utf-8

# this code if from https://dash.plot.ly/getting-started website 

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

df=pd.read_csv("https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv")
#df = df.drop(columns='Reasonforprotest')

def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +
        
        #Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#A1B1C1',
    'text': '#7fDBFF'
}


# creating app layout
app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['continent'] == i]['gdp per capita'],
                    y=df[df['continent'] == i]['life expectancy'],
                    text=df[df['continent'] == i]['country'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size' : 15,
                        'line': {'width' : 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.continent.unique()
            ],
            'layout' : go.Layout(
                xaxis={'type': 'log', 'title' : 'GDP Per Capita'},
                yaxis={'title' : 'Life Expectancy'},
                margin={'l' : 40, 'b' : 40, 't': 10, 'r' : 10},
                legend={'x' : 0, 'y' : 1},
                hovermode='closest'
            )
        }
    )
])
# if running app gives port number in use change port to a different portn no
if __name__ == '__main__':
	app.run_server(debug=True, port='8080')