import dash                     # pip install dash
from dash.dependencies import Input, Output, State
from dash import dcc, html# import dash_html_components as html
import plotly.express as px     # pip install plotly==5.2.2
import pandas as pd             # pip install pandas
import plotly.graph_objs as go
# Data: https://www.dallasopendata.com/Services/Animals-Inventory/qgg6-h4bd

df = pd.read_csv("Univ2.csv")
print(df.head())


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div([
    html.H1("University Dashboard (Dash Plotly)", style={"textAlign":"center"}),
    html.Hr(),
    html.P("Choose State of interest:"),
    html.Div(html.Div([
        dcc.Dropdown(id='state', clearable=False,
                     value="AK",
                     options=[{'label': x, 'value': x} for x in
                              df["State"].unique()]),
    ],className="two columns"),className="row"),

    html.Div(id="output-div", children=[]),
])


@app.callback(Output(component_id="output-div", component_property="children"),
              Input(component_id="state", component_property="value"),
)
def make_graphs(state_chosen):
    # HISTOGRAM
    df_hist = df[df["State"]==state_chosen]
    print(df_hist.head())
    fig_hist = px.bar(df_hist, x="total_cost", y = 'College_Name')

    # STRIP CHART
    fig_strip = px.scatter_3d(df_hist, x="#_appl._accepted", y="#_appli._rec'd", z ='Graduation_rate', hover_name=df_hist['College_Name'])



    return [
        html.Div([
            html.Div([dcc.Graph(figure=fig_hist)], className="six columns"),
            html.Div([dcc.Graph(figure=fig_strip)], className="six columns"),
        ], className="row"),
        html.Hr()
    ]


if __name__ == '__main__':
    app.run_server(debug=True)