from flask import Flask, jsonify, make_response
from flask_restx import Api
from db import seed_db
from dotenv import load_dotenv
import os
from apis.v1.japanese import api as jap_ns
from apis.v1.api_models import root_ns as models
from db.db import db
from flask_cors import CORS

load_dotenv()

def create_db(app):
    db.init_app(app)    
    seed_db.seed(db,app)

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}/{os.getenv('POSTGRES_DB')}"
    create_db(app)
    return app



app = create_app()
CORS(app)

api = Api(app, version='1.2.0', title='Japanese Vocabulary API', 
                description='This is a simple API for japanese vocabulary. There are categories, words and alphabets. Each word have a category and is writen in one alphabets. \
                But in the case of one word is writen in kanji, the word also have his phonetic writen in hiragana. \
                For example: 魚 is the kanji for "Fish", and his phonetic is さかな.    -    \
                If you wanna contribute with vocabulary or with code, please visit the github repository',



                contact='Demian Daniel Durán',
                contact_url='https://www.linkedin.com/in/durandemiandaniel/',
                contact_email='demi.4d@gmail.com',
                

                
                license='Repository: https://github.com/4Dante-senpai/japanese-vocabulary-api',
                terms_url='https://github.com/4Dante-senpai/japanese-vocabulary-api',
                )

api.add_namespace(models)
api.add_namespace(jap_ns)

@app.route('/healthy')
def Home():
    response = make_response(jsonify('Healthy check'), 200)
    return response

if __name__ == '__main__':
    print(os.environ)
    app.run(debug=True, host="0.0.0.0")