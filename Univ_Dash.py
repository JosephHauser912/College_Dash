import dash                     # pip install dash
from dash.dependencies import Input, Output, State
from dash import dcc, html# import dash_html_components as html
import plotly.express as px     # pip install plotly==5.2.2
import pandas as pd             # pip install pandas
# Data: https://www.dallasopendata.com/Services/Animals-Inventory/qgg6-h4bd

df = pd.read_csv("Univ2.csv")
# df["intake_time"] = pd.to_datetime(df["intake_time"])
# df["intake_time"] = df["intake_time"].dt.hour
# print(df.head())


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
######################################
app.layout = html.Div([
    html.Label('Select State:'),
    dcc.Dropdown(
        id='state-dropdown',
        options=[
            {'label': category, 'value': category} for category in df['State'].unique()
        ],
        value=None,
        clearable=False
    ),
    html.Br(),
    html.Label('Select College:'),
    dcc.Dropdown(
        id='college-dropdown',
        options=[],
        value=None,
        clearable=False
    ),html.Div(id="output-div", children=[])
])

######################################################



@app.callback(Output(component_id="output-div",component_property="children"),
Input(component_id="state-dropdown", component_property="value"),
)
def update_item_options(selected_category):
    if selected_category is None:
        raise dash.exceptions.PreventUpdate

    # Get options for the selected category
    options = [{'label': item, 'value': item} for item in df[selected_category]]
    return options
def make_graphs(state_chosen):
    # HISTOGRAM
    df_hist = df[df["State"]==state_chosen]
    fig_hist = px.histogram(df_hist, x = 'in-state_tuition')
    fig_hist.update_xaxes(categoryorder="total descending")

    # # STRIP CHART
    # fig_strip = px.strip(df_hist, x="animal_stay_days", y="intake_type")

    # # SUNBURST
    # df_sburst = df.dropna(subset=['chip_status'])
    # df_sburst = df_sburst[df_sburst["intake_type"].isin(["STRAY", "FOSTER", "OWNER SURRENDER"])]
    # fig_sunburst = px.sunburst(df_sburst, path=["State", "intake_type", "chip_status"])

    # # Empirical Cumulative Distribution
    # df_ecdf = df[df["State"].isin(["DOG","CAT"])]
    # fig_ecdf = px.ecdf(df_ecdf, x="animal_stay_days", color="State")

    # # LINE CHART
    # df_line = df.sort_values(by=["intake_time"], ascending=True)
    # df_line = df_line.groupby(
    #     ["intake_time", "State"]).size().reset_index(name="count")
    # fig_line = px.line(df_line, x="intake_time", y="count",
    #                    color="State", markers=True)

    return [
        html.Div([
            html.Div([dcc.Graph(figure=fig_hist)], className="six columns"),
            # html.Div([dcc.Graph(figure=fig_strip)], className="six columns"),
        ], className="row"),
        html.H2("All Animals", style={"textAlign":"center"}),
        html.Hr(),
    # #     html.Div([
    # #         html.Div([dcc.Graph(figure=fig_sunburst)], className="six columns"),
    # #         html.Div([dcc.Graph(figure=fig_ecdf)], className="six columns"),
    # #     ], className="row"),
    # #     html.Div([
    # #         html.Div([dcc.Graph(figure=fig_line)], className="twelve columns"),
    # #     ], className="row"),
    ]


if __name__ == '__main__':
    app.run_server(debug=True)