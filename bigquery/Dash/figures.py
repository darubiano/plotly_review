import plotly.express as px
import plotly.graph_objects as go


def figure_scatter_mapbox(dataset,center={"lat": 4.6580945, "lon": -74.1028763},zoom=9.6):
    fig = px.scatter_mapbox(dataset, lat="latitude_centroid", lon="longitude_centroid",
                            color='population', size='population', size_max=9, zoom=zoom,
                            center=center, color_continuous_scale='Jet')
    fig.update_layout(mapbox_style="open-street-map", margin={"r": 0, "t": 0, "l": 0, "b": 0},
                    template='plotly_dark', height=750)
    return fig


def figure_table(dataset):
    return go.Figure(data=[go.Table(
        header=dict(values=list(dataset.columns), align='left'),
        cells=dict(values=dataset.values.T, align='left'))
    ])
