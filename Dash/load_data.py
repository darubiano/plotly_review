import plotly.express as px

def load_data_gapminder():
    return px.data.gapminder().query("continent=='Americas'")