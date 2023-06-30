from flask_restx import Resource, reqparse, Namespace
from flask import jsonify, abort
from db.service import words_service
from db.service import categories_service
from db.utils.helpers_db import validate_category
from . import api_models

api = Namespace('v1/', description='Japanese vocabulary')


parser = reqparse.RequestParser()
parser.add_argument('page', type=int, help='Page to look')

@api.route('/words/')
class AllWords(Resource):
    '''Return all words paginated by 20 words per page'''
    @api.doc('Return all words paginated by 20 words per page', model=api_models.paginated_words)
    @api.doc(responses={404: 'Page not found or out of range. Try without any parameter to see how many pages there are.'})
    @api.expect(parser)
    def get(self):
        '''Return all words paginated by 20 words per page'''
        args = parser.parse_args()
        response = words_service.all_words(args['page'])
        if response == 404:
            return abort(404, 'Page not found or out of range. Try without any parameter to see how many pages there are.')
        return jsonify(response)
    
@api.route('/words/<int:id>')
class AllWords(Resource):
    '''Return one word with that ID'''
    @api.doc('Return one word with that ID', model=api_models.word)
    @api.doc(responses={404: 'ID not found'})
    def get(self, id):
        '''Return one word with that ID'''
        response = words_service.specific_word(id)
        if response == 404:
            return abort(404, 'ID not found')
        return jsonify(response)
    
@api.route('/words/random/')
class AllWords(Resource):
    '''Return five random words'''
    @api.doc('Return five random words', model=api_models.words)
    def get(self):
        '''Return five random words'''
        response = words_service.random_word()
        if response == 404:
            return abort(404, 'ID not found')
        return jsonify(response)
    
@api.route('/categories/')
class Categories(Resource):
    '''Return a list of all the categories'''
    @api.doc('Return a list of all the categories', model=api_models.categories)
    def get(self):
        '''Return a list of all the categories'''
        categories = categories_service.all_categories()
        return jsonify(categories)
    
@api.route('/words/<string:category>')
class Categories(Resource):
    '''Return all the words from one category'''
    @api.doc('Return all the words from one category', model=api_models.paginated_words)
    @api.doc(responses={404: 'Page not found or out of range. Try without any parameter to see how many pages there are.'})
    @api.expect(parser)
    def get(self, category):
        '''Return all the words from one category'''
        args = parser.parse_args()
        if validate_category(category):
            response = categories_service.get_all_from_category(category, args['page'])
            if response == 404:
                return abort(404, 'Page not found or out of range. Try without any parameter to see how many pages there are.')
            return jsonify(response)
        else:
            return abort(404, 'Category dosent exist')
    
@api.route('/words/higarana/')
class AllHigarana(Resource):
    '''Return all higarana words paginated by 20 words per page'''
    @api.doc('Return all higarana words paginated by 20 words per page', model=api_models.paginated_words)
    @api.doc(responses={404: 'Page not found or out of range. Try without any parameter to see how many pages there are.'})
    @api.expect(parser)
    def get(self):
        '''Return all higarana words paginated by 20 words per page'''
        args = parser.parse_args()
        response = words_service.all_higarana(args['page'])
        if response == 404:
            return abort(404, 'Page not found or out of range. Try without any parameter to see how many pages there are.')
        return jsonify(response)
    
@api.route('/words/hiragana/<string:category>')
class Categories(Resource):
    '''Return all the hiragana words from one category paginated by 20 words per page'''
    @api.doc('Return all the hiragana words from one category paginated by 20 words per page', model=api_models.paginated_words)
    @api.doc(responses={404: 'Page not found or out of range. Try without any parameter to see how many pages there are.'})
    @api.expect(parser)
    def get(self, category):
        '''Return all the hiragana words from one category paginated by 20 words per page'''
        args = parser.parse_args()
        if validate_category(category):
            response = categories_service.get_all_hiragana_from_category(category, args['page'])
            if response == 404:
                return abort(404, 'Page not found or out of range. Try without any parameter to see how many pages there are.')
            return jsonify(response)
        else:
            return abort(404, 'Category dosent exist')
    
@api.route('/words/katakana/')
class AllKatakana(Resource):
    '''Return all katakana words paginated by 20 words per page'''
    @api.doc('Return all higarana words paginated by 20 words per page', model=api_models.paginated_words)
    @api.doc(responses={404: 'Page not found or out of range. Try without any parameter to see how many pages there are.'})
    @api.expect(parser)
    def get(self):
        '''Return all katakana words paginated by 20 words per page'''
        args = parser.parse_args()
        response = words_service.all_katakana(args['page'])
        if response == 404:
            return abort(404, 'Page not found or out of range. Try without any parameter to see how many pages there are.')
        return jsonify(response)
    
@api.route('/words/katakana/<string:category>')
class Categories(Resource):
    '''Return all the katakana words from one category paginated by 20 words per page'''
    @api.doc('Return all the katakana words from one category paginated by 20 words per page', model=api_models.paginated_words)
    @api.doc(responses={404: 'Page not found or out of range. Try without any parameter to see how many pages there are.'})
    @api.expect(parser)
    def get(self, category):
        '''Return all the katakana words from one category paginated by 20 words per page'''
        args = parser.parse_args()
        if validate_category(category):
            response = categories_service.get_all_katakana_from_category(category, args['page'])
            if response == 404:
                return abort(404, 'Page not found or out of range. Try without any parameter to see how many pages there are.')
            return jsonify(response)
        else:
            return abort(404, 'Category dosent exist')

@api.route('/words/kanji/')
class AllKanji(Resource):
    '''Return all kanji words paginated by 20 words per page'''
    @api.doc('Return all kanji words paginated by 20 words per page', model=api_models.paginated_words)
    @api.doc(responses={404: 'Page not found or out of range. Try without any parameter to see how many pages there are.'})
    @api.expect(parser)
    def get(self):
        '''Return all kanji words paginated by 20 words per page'''
        args = parser.parse_args()
        response = words_service.all_kanji(args['page'])
        if response == 404:
            return abort(404, 'Page not found or out of range. Try without any parameter to see how many pages there are.')
        return jsonify(response)
    
@api.route('/words/kanji/<string:category>')
class Categories(Resource):
    '''Return all the kanji words from one category paginated by 20 words per page'''
    @api.doc('Return all the kanji words from one category paginated by 20 words per page', model=api_models.paginated_words)
    @api.doc(responses={404: 'Page not found or out of range. Try without any parameter to see how many pages there are.'})
    @api.expect(parser)
    def get(self, category):
        '''Return all the kanji words from one category paginated by 20 words per page'''
        args = parser.parse_args()
        if validate_category(category):
            response = categories_service.get_all_kanji_from_category(category, args['page'])
            if response == 404:
                return abort(404, 'Page not found or out of range. Try without any parameter to see how many pages there are.')
            return jsonify(response)
        else:
            return abort(404, 'Category dosent exist')

