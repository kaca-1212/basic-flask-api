from flask import request
from flask_restplus import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import TechnologyDto
from ..service.technology_service import save_new_technology, get_all_technologies, delete_a_technology

api = TechnologyDto.api
_technology = TechnologyDto.technology


@api.route('/')
class TechnologyList(Resource):
    @api.doc('list of technologies')
    @api.marshal_list_with(_technology, envelope='data')
    def get(self):
        """List all technologies"""
        return get_all_technologies()

    @api.expect(_technology, validate=True)
    @api.response(200, 'Technology successfully added.')
    @admin_token_required
    @api.doc('add a new technology', params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
    @api.marshal_with(_technology)
    def post(self):
        """Adding a new Technology """
        data = request.json
        return save_new_technology(data=data)

    @api.expect(_technology, validate=True)
    @api.response(200, 'Technology successfully deleted.')
    @api.doc('delete a technology', params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
    def delete(self):
        """Deleting a Technology """
        data = request.json
        return delete_a_technology(data=data)
