from flask_restful import Resource
from models.client import Client
from constants import USER_REQUIRED_FIELDS
from models.utils import get_all, get_instance, add_instance, get_full_client_data
from flask import request


class ClientView(Resource):
    def get(self, client_id):
        client_data = get_instance(Client, client_id)
        if client_data:
            return get_full_client_data(client_data)
        return {'success': False}, 404


class ClientListView(Resource):
    def get(self):
        resp = list()
        clients_data = get_all(Client)
        for client in clients_data:
            resp.append(get_full_client_data(client))
        return resp

    def post(self):
        content = request.json
        if set(USER_REQUIRED_FIELDS) == set(content.keys()):
            data = add_instance(Client, **content)
            return data.id
        return {'success': False, 'message': 'Not all the required fields are provided'}, 400
