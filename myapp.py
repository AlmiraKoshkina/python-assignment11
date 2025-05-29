import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Load the built-in Gapminder dataset
df = px.data.gapminder()

# Get the list of unique countries for the dropdown menu
countries = df['country'].unique()

# Initialize Dash application
app = dash.Dash(__name__)
server = app.server  # Required for deployment on Render.com

# App layout
app.layout = html.Div([
    html.H1("GDP Per Capita Over Time"),
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': c, 'value': c} for c in countries],
        value='Canada'  # Default selected country
    ),
    dcc.Graph(id='gdp-growth')
])

# Callback — updates the graph when a different country is selected
@app.callback(
    Output('gdp-growth', 'figure'),
    Input('country-dropdown', 'value')
)
def update_graph(selected_country):
    filtered_df = df[df['country'] == selected_country]
    fig = px.line(
        filtered_df,
        x='year',
        y='gdpPercap',
        title=f"GDP Per Capita for {selected_country}"
    )
    return fig

# Run the app locally
if __name__ == '__main__':
    app.run_server(debug=True)
