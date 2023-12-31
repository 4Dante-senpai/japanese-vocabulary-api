import pandas as pd
from io import BytesIO
import requests
from sqlalchemy.types import Integer
from .utils import alter_tables
import os

def seed(db, app):
    sheet_id = "1_fjQaRAUUzwDe6iagQKxyK_uGeyJhvLyzpOWEO6fPAY"
    sheet_config = "config"

    url_sheets = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_config}"
    req = requests.get(url_sheets)
    data = req.content
    df_categories = pd.read_csv(BytesIO(data), encoding='utf-8')
    config_index = df_categories[df_categories['category'] == 'config'].index
    df_categories = df_categories.drop(config_index, axis=0)

    categories = df_categories.to_dict().get('category')
    categories_spanish = df_categories.to_dict().get('spanish')

    list_df = []
    categories_spanish_index = 0

    for category in categories.values():
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={category}"
        req = requests.get(url)
        data = req.content
        df_local = pd.read_csv(BytesIO(data), encoding='utf-8', index_col=False)
        df_local['category'] = category
        df_local['category_spanish'] = list(categories_spanish.values())[categories_spanish_index]
        list_df.append(df_local)
        categories_spanish_index += 1

    df_final = pd.concat(list_df, ignore_index=True)

    with app.app_context():
        try:
            engine = db.engine
            df_final.to_sql('words', engine.connect(), index_label='id', dtype={'id': Integer()}, if_exists="replace")
            df_categories.to_sql('categories', engine.connect(), index_label='id', dtype={'id': Integer()}, if_exists="replace")


            #Workaround to SQLAlchemy ALTER
            alter_tables.set_pk({'words': 'id' ,'categories': 'category'})
            
        except Exception as e:
            print(e)