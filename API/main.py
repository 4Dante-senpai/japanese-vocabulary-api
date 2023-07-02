from flask import Flask
from flask_restx import Api
from db import seed_db
from db import create_db
from dotenv import load_dotenv
import os
from apis.v1.japanese import api as jap_ns
from apis.v1.api_models import root_ns as models
from db.db import db

load_dotenv()

create_db.create_japanese()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}/{os.getenv('POSTGRES_DB')}"
    return app

def create_db():
    while True:
        try:
            db.init_app(app)    
            seed_db.seed(db,app)
            print(os.environ)
            break
        except Exception as e:
            print(e)
            print('Triying again in 20 seconds')

app = create_app()

api = Api(app, version='1.0', title='Japanese Vocabulary API', 
                description='A simple japanese vocabulary API')

api.add_namespace(models)
api.add_namespace(jap_ns)

if __name__ == '__main__':
    create_db()
    app.run(debug=True, host="0.0.0.0")