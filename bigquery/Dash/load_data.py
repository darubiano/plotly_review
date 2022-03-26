
import os
import pandas as pd
import bigquery as bg

# Cargar datos
#dataset = bg.excecute_query(qs.population_by_country('Colombia'))
def load_data(query_string, dataset_name):
    file = f"./data/{dataset_name}.pkl.zip"
    if os.path.isfile(file):
        print('cargando datos desde archivo')
        dataset = pd.read_pickle(file)
        print(f'Size: {dataset.size}')
    else:
        print('cargando datos desde bigquery')
        dataset = bg.excecute_query(query_string)
        print(f'Size: {dataset.size}')
        dataset.to_pickle(file,compression="zip")
    return dataset