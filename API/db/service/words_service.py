from db.db import db
from db.models.Words import Words
from db.utils.helpers_db import generate_metadata
from  sqlalchemy.sql.expression import func 

def random_word():
    page = db.paginate(db.select(Words).order_by(func.random()), per_page=5)

    if page.page > page.pages:
        return (404)
    
    words = []
    for word in page.items:
        words.append(word.to_dict())

    return({'words' : words})

def all_words(p):
    page = db.paginate(db.select(Words), page=p, error_out=False)

    if page.page > page.pages:
        return (404)

    meta = generate_metadata(page)

    words = []
    for word in page.items:
        words.append(word.to_dict())

    return ({'data': words, 'metadata': meta})

def all_higarana(p):
    page = db.paginate(db.select(Words).where(Words.is_katakana == 0), page=p, error_out=False)

    if page.page > page.pages:
        return (404)

    meta = generate_metadata(page)

    words = []
    for word in page.items:
        words.append(word.to_dict())

    return ({'data': words, 'metadata': meta})



def all_katakana(p):
    page = db.paginate(db.select(Words).where(Words.is_katakana == 1), page=p, error_out=False)

    if page.page > page.pages:
        return (404)

    meta = generate_metadata(page)

    words = []
    for word in page.items:
        words.append(word.to_dict())

    return ({'data': words, 'metadata': meta})

def all_kanji(p):
    page = db.paginate(db.select(Words).where(Words.kanji != ''), page=p, error_out=False)

    if page.page > page.pages:
        return (404)

    meta = generate_metadata(page)

    words = []
    for word in page.items:
        words.append(word.to_dict())

    return ({'data': words, 'metadata': meta})

def specific_word(id):

    word_page = db.paginate(db.select(Words).where(Words.id == id), per_page=1, error_out=False)

    if word_page.page > word_page.pages:
        return (404)
    
    for word in word_page.items:
        return (word.to_dict())
    
def get_kanji_random():
    page = db.paginate(db.select(Words).where(Words.kanji != None).order_by(func.random()), per_page=5)

    if page.page > page.pages:
        return (404)

    words = []
    for word in page.items:
        words.append(word.to_dict())

    return({'words' : words})

def get_higarana_random():
    page = db.paginate(db.select(Words).where(Words.is_katakana == 0).order_by(func.random()), per_page=5)

    if page.page > page.pages:
        return (404)

    words = []
    for word in page.items:
        words.append(word.to_dict())

    return({'words' : words})

def get_katakana_random():
    page = db.paginate(db.select(Words).where(Words.is_katakana == 1).order_by(func.random()), per_page=5)

    if page.page > page.pages:
        return (404)

    words = []
    for word in page.items:
        words.append(word.to_dict())

    return({'words' : words})