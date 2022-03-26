import pandas_gbq
from google.oauth2 import service_account

# ubicacion del archivo json
credentials = service_account.Credentials.from_service_account_file('../bigquery.json')
#
def excecute_query(query_string):
    df = pandas_gbq.read_gbq(query_string, project_id='bigquery-345316',
                                credentials=credentials,use_bqstorage_api=True)
    print(f"consultando sql a bigquery {df.size}")
    return df