import figures as fg
import querys as qs
import load_data as ld
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Configuracion de la pagina
app = Dash(__name__, external_stylesheets=[
           dbc.themes.DARKLY], assets_folder='assets')
app.title = 'Dashboard'
# Cargar datos
#dataset_bogota = ld.load_data(qs.POPULATION_BOGOTA, 'population_bogota')
#dataset_colombia = ld.load_data(qs.population_by_country('Colombia'),'population_colombia')
dataset_japan = ld.load_data(qs.population_by_country('Japan'), 'population_japan')
#dataset_world = ld.load_data(qs.POPULATION_WORLD, 'population_world')

# Main pagina
app.layout = html.Div(
    style={'textAlign': 'center'},
    children=[
        #html.H1('World Population Dashboard'),
        #dcc.Graph(figure= fg.figure_scatter_mapbox(dataset_bogota, 'Poblacion de Bogota')),
        html.H1('Poblacion de Japon'),
        dcc.Graph(figure=fg.figure_scatter_mapbox(dataset_japan,{"lat": 35.7457575, "lon":140.3554467}, 6.15)),
        #dcc.Graph(figure= fg.figure_table(dataset_world)),
        #dcc.Graph(figure=fg.figure_scatter_mapbox(dataset_world[:1000000],{"lat": 0.0, "lon":0.0}, 1)),
    ]
)

if __name__ == '__main__':
    # Turn off reloader if inside Jupyter
    app.run_server(debug=True, use_reloader=True)
