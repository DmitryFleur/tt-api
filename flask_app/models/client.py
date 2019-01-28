from . import db
from sqlalchemy_serializer import SerializerMixin


class Client(db.Model, SerializerMixin):
    __table_args__ = {"schema": "clients"}
    __tablename__ = 'tt_clients'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    last_name = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    dob = db.Column(db.Date)
    social_status_id = db.Column(db.Integer)
    gender = db.Column(db.String(1))

    def __repr__(self):
        return '%s %s' % (self.first_name, self.last_name)
