# https://dash.plotly.com/dash-html-components/center 
import figures as fg
import load_data as ld
from dash import Dash,Input,Output,html,dcc
#

#Cargar figura
app = Dash(__name__)

@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    return f'Output: {input_value}'

# Main pagina
app.layout = html.Div([
    html.Center(html.H1('Dashboard')),
    dcc.Graph(figure=fg.figure_line(ld.load_data_gapminder())),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', type='text', value='Enter text')
    ]),
    html.Br(),
    html.Div(id='my-output',)
])


if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter