import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import base64

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("CSV to Bar Chart"),
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    dcc.Graph(id='bar-chart')
])

# Define callback to update the bar chart
@app.callback(
    Output('bar-chart', 'figure'),
    [Input('upload-data', 'contents'),
     Input('upload-data', 'filename')]
)
def update_bar_chart(contents, filename):
    if contents is None:
        return dash.no_update
    
    # Read the contents of the uploaded CSV file
    content_type, content_string = contents[0].split(',')
    decoded = base64.b64decode(content_string)
    df = pd.read_csv('expensive_ten.csv')
    
    # Create the bar chart using Plotly Express
    fig = px.bar(df, x=df.columns[0], y=df.columns[1], title='Bar Chart')
    
    return fig

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)