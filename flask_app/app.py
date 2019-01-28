from flask import Flask
from flask_restful import Api
from models import db
from views.users import ClientListView, ClientView

app = Flask(__name__)
api = Api(app)
POSTGRES_CREDENTIALS = {
    'user': 'postgres',
    'pw': 'passw0rd@1',
    'db': 'postgres',
    'host': 'db',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % \
                                        POSTGRES_CREDENTIALS
db.init_app(app)


api.add_resource(ClientListView, '/clients')
api.add_resource(ClientView, '/clients/<int:client_id>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
