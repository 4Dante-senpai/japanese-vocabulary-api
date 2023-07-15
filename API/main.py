from flask import Flask, jsonify, make_response
from flask_restx import Api
from db import seed_db
from dotenv import load_dotenv
import os
from apis.v1.japanese import api as jap_ns
from apis.v1.api_models import root_ns as models
from db.db import db
from time import sleep

load_dotenv()

def create_db(app):
    while True:
        try:
            db.init_app(app)    
            seed_db.seed(db,app)
            print(os.environ)
            break
        except Exception as e:
            sleep(20)
            print(e)
            print('Triying again in 20 seconds')

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}/{os.getenv('POSTGRES_DB')}"
    create_db(app)
    return app



app = create_app()

api = Api(app, version='1.0', title='Japanese Vocabulary API', 
                description='A simple japanese vocabulary API')

api.add_namespace(models)
api.add_namespace(jap_ns)

@app.route('/healthy')
def Home():
    response = make_response(jsonify('Healthy check'), 200)
    return response

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")