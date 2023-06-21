import pandas as pd
from io import BytesIO
import requests

def seed(db, app):
    sheet_id = "16lEzU_kJiVdlp77g-czverzyZ2q2i0iOmWW_fAwCeus"
    sheets = ["foods", "verbs", "people", "numbers", "dates", "adjetives", "daily_use"]

    list_df = []

    for sheet in sheets:
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet}"
        req = requests.get(url)
        data = req.content
        df_local = pd.read_csv(BytesIO(data), encoding='utf-8', index_col=False)
        df_local['category'] = sheet
        list_df.append(df_local)

    df_final = pd.concat(list_df, ignore_index=True)

    with app.app_context():
        try:
            engine = db.get_engine()
            #This create a table with "bigInt" and "text"
            #Maybe I can use the model without lose performance with pandas
            df_final.to_sql('words', engine.connect())
        except Exception as e:
            print(e)