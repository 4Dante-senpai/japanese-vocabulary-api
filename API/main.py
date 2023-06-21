from flask import Flask
from flask import jsonify
from db import seed_db
from db import create_db
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import os

load_dotenv()

db = SQLAlchemy()
create_db.create_japanese()

def create_app():
#def create_app(enviroment):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}/{os.getenv('POSTGRES_DB')}"
    return app

app = create_app()

@app.route('/api/v1/users', methods=['GET'])
def get_users():
    response = {'message': 'success'}
    return jsonify(response)

if __name__ == '__main__':
    db.init_app(app)
    seed_db.seed(db,app)
    app.run(debug=True, host="0.0.0.0")