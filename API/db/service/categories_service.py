from db.db import db
from db.models.Words import Words
from db.models.Categories import Categories
from db.utils.helpers_db import generate_metadata
from sqlalchemy.sql.expression import func 

def all_categories():
    page = db.paginate(db.select(Categories), per_page=500)

    categories = []
    for category in page.items:
        print(category)
        categories.append(category.get_pk())

    print(categories)

    return ({'categories': categories})

def get_all_from_category(category, p):
    page = db.paginate(db.select(Words).where(Words.category == category), page=p, error_out=False)

    if page.page > page.pages:
        return (404)

    meta = generate_metadata(page)

    words = []
    for word in page.items:
        words.append(word.to_dict())

    return ({'data': words, 'metadata': meta})

def get_all_hiragana_from_category(category, p):
    page = db.paginate(db.select(Words).where((Words.category == category) & (Words.is_katakana == 0)), page=p, error_out=False)

    if page.page > page.pages:
        return (404)

    meta = generate_metadata(page)

    words = []
    for word in page.items:
        words.append(word.to_dict())

    return ({'data': words, 'metadata': meta})

def get_all_katakana_from_category(category, p):
    page = db.paginate(db.select(Words).where((Words.category == category) & (Words.is_katakana == 1)), page=p, error_out=False)

    if page.page > page.pages:
        return (404)

    meta = generate_metadata(page)

    words = []
    for word in page.items:
        words.append(word.to_dict())

    return ({'data': words, 'metadata': meta})

def get_all_kanji_from_category(category, p):
    page = db.paginate(db.select(Words).where((Words.category == category) & (Words.kanji != None)), page=p, error_out=False)

    if page.page > page.pages:
        return (404)

    meta = generate_metadata(page)

    words = []
    for word in page.items:
        words.append(word.to_dict())

    return ({'data': words, 'metadata': meta})

def get_random_from_category(category):
    page = db.paginate(db.select(Words).where(Words.category == category).order_by(func.random()), per_page=5)

    if page.page > page.pages:
        return (404)

    words = []
    for word in page.items:
        words.append(word.to_dict())

    return({'words' : words})

# _____

def get_kanji_random_from_category(category):
    page = db.paginate(db.select(Words).where((Words.category == category) & (Words.kanji != None)).order_by(func.random()), per_page=5)

    if page.page > page.pages:
        return (404)

    words = []
    for word in page.items:
        words.append(word.to_dict())

    return({'words' : words})

def get_higarana_random_from_category(category):
    page = db.paginate(db.select(Words).where((Words.category == category) & (Words.is_katakana == 0)).order_by(func.random()), per_page=5)

    if page.page > page.pages:
        return (404)

    words = []
    for word in page.items:
        words.append(word.to_dict())

    return({'words' : words})

def get_katakana_random_from_category(category):
    page = db.paginate(db.select(Words).where((Words.category == category) & (Words.is_katakana == 1)).order_by(func.random()), per_page=5)

    if page.page > page.pages:
        return (404)

    words = []
    for word in page.items:
        words.append(word.to_dict())

    return({'words' : words})


