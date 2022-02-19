import plotly.express as px

def figure_line(dataset):
    fig = px.line(dataset[dataset['country'].str.contains('C')],
                    x='year',y ='lifeExp', color='country')
    fig.update_layout(template='plotly_dark')
    fig.update_traces(mode='lines+markers')
    return fig

