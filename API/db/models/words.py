import sqlalchemy as sa
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Words(db.Model):
    id = sa.Column(db.Integer, primary_key=True)
    kanji = sa.Column(db.String(64))
    phonetics = sa.Column(db.String(64))
    pronunciation = sa.Column(db.String(64))
    english = sa.Column(db.String(64))
    spanish = sa.Column(db.String(64))
    category = sa.Column(db.String(64))
    is_katakana = sa.Column(db.Boolean)

    def __repr__(self):
        return f'<Words {self.pronunciation} {self.english}>'