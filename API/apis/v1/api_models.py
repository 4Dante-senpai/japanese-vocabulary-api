from flask_restx import fields, Api

root_api = Api()
root_ns = root_api.namespace('models')


word = root_ns.model('Word', {
    'id': fields.Integer,
    'kanji': fields.String,
    'phonetics': fields.String,
    'pronunciation': fields.String,
    'english': fields.String,
    'spanish': fields.String,
    'is_katakana': fields.Boolean(default=False),
    'category': fields.String,
    'category_spanish': fields.String
})

words = root_ns.model('Words', {
    'words' : fields.List(fields.Nested(word))
})

meta = root_ns.model('Metadata', {
    'page': fields.Integer,
    'pages': fields.Integer,
    'per_page': fields.Integer,
    'total_count': fields.Integer,
    'prev_page': fields.Integer,
    'next_page': fields.Integer,
    'has_prev': fields.Boolean,
    'has_next': fields.Boolean
})

paginated_words = root_ns.model('Paginated_words', {
    'data': fields.Nested(words),
    'metadata': fields.Nested(meta)
})

categories = root_ns.model('Categories', {
    'categories': fields.List(fields.String)
    })