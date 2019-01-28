from . import db
from sqlalchemy_serializer import SerializerMixin


class Dictionary(db.Model, SerializerMixin):
    __table_args__ = {"schema": "clients"}
    __tablename__ = 'tt_dictionary'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    category = db.Column(db.String(255))
    str_id = db.Column(db.String(50), nullable=True)
    int_id = db.Column(db.Integer)
    value = db.Column(db.String(255))

    def __repr__(self):
        return '%s: %s' % (self.category, self.value)
