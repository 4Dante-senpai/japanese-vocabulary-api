import sqlalchemy as sa
from ..db import db

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
    
    def to_dict(self):
        word = {}
        word['id'] = self.id
        word['kanji'] = self.kanji
        word['phonetics'] = self.phonetics
        word['pronunciation'] = self.pronunciation
        word['english'] = self.english
        word['spanish'] = self.spanish
        word['category'] = self.category
        word['is_katakana'] = True if self.is_katakana == 1 else False 
        return word