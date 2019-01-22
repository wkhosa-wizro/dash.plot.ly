# coding: utf-8

# this code if from https://dash.plot.ly/getting-started website 

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.read_csv("https://data.code4sa.org/api/views/7y3u-atvk/rows.csv?accessType=DOWNLOAD")
df = df.drop(columns='Reasonforprotest')

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
app.layout = html.Div(children=[
    html.H4(children='SA Protest Data 2013-2014', 
           style={'textAlign': 'center',
                 'color': colors['text']
                 }
           ),
    generate_table(df)])
    
# if running app gives port number in use change port to a different portn no
if __name__ == '__main__':
	app.run_server(debug=True, port='8080')