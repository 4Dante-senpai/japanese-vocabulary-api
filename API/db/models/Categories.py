import sqlalchemy as sa
from ..db import db

class Categories(db.Model):
    id = sa.Column(db.Integer, primary_key=True)
    category = sa.Column(db.String(64))

    def __repr__(self):
        return f'<Category {self.id} {self.category}>'
    
    def to_dict(self):
        category = {}
        category['id'] = self.id
        category['category'] = self.category
        return category
    
    def get_pk(self):
        return self.category