import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load data from CSV
df = pd.read_csv("assignment11/sales.csv")

# Create Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("Sales and Expenses Analysis"),
    
    dcc.Dropdown(
        id="metric-dropdown",
        options=[
            {"label": "Sales", "value": "Sales"},
            {"label": "Expenses", "value": "Expenses"}
        ],
        value="Sales"
    ),

    dcc.Graph(id="line-graph")
])

# Callback for updating the chart
@app.callback(
    Output("line-graph", "figure"),
    [Input("metric-dropdown", "value")]
)
def update_chart(metric):
    fig = px.line(df, x="Month", y=metric, title=f"{metric} by Month")
    return fig

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
