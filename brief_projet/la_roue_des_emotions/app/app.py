import dash
import dash_bootstrap_components as dbc

#external_stylesheets = ["https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"]
#'https://codepen.io/chriddyp/pen/bWLwgP.css',

external_stylesheets = [dbc.themes.LUX]

app = dash.Dash(external_stylesheets=external_stylesheets)
server = app.server
app.config.suppress_callback_exceptions = True

# app = dash.Dash(__name__, suppress_callback_exceptions=True)
# server = app.server