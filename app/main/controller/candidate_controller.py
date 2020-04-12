from flask import request
from flask_restplus import Resource

from app.main.util.decorator import admin_token_required, token_required
from ..util.dto import CandidateDto, TechnologyDto
from ..service.candidate_service import save_new_candidate, get_all_candidates, add_technologies, delete_technologies, \
    delete_candidate, search_candidate_by_age, search_candidates_by_tech
from ..service.auth_helper import Auth

api = CandidateDto.api
_candidate = CandidateDto.candidate
_technology = TechnologyDto.technology


@api.route('/')
class CandidateList(Resource):
    @api.doc('list_of_registered_candidates', params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
    @admin_token_required
    @api.marshal_list_with(_candidate, mask='cid,mail,name,surname,age,city,birth_year,technologies')
    def get(self):
        """List all registered candidates"""
        return get_all_candidates()

    @api.expect(_candidate, validate=True)
    @api.response(201, 'User successfully created.')
    @api.doc('create a new candidate')
    def post(self):
        """Creates a new Candidate """
        data = request.json
        return save_new_candidate(data=data)


@api.route('/<candidate_id>')
class Candidate(Resource):
    @api.doc('delete candidate', params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
    @admin_token_required
    @api.response(200, 'Candidate successfully deleted.')
    def delete(self, candidate_id):
        """Deleting a candidate"""
        return delete_candidate(candidate_id)


@api.route('/technology/<tech_id>')
class CandidateTechnology(Resource):
    @api.doc('list of canidates with specific technology', params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
    @admin_token_required
    @api.marshal_list_with(_candidate, mask='cid,email,name,surname,age,city,birth_year,technologies')
    def get(self, tech_id):
        """List all candidates with required technology"""
        return search_candidates_by_tech(tech_id=tech_id)

    @api.doc('add technologies for a candidate', params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
    @token_required
    @api.response(201, 'Technologies successfully added.')
    def put(self, tech_id):
        """Adding technologies for a candidate"""
        if not isinstance(Auth.get_roles(request), str):
            candidate_id, _ = Auth.get_roles(request)
            if candidate_id:
                return add_technologies(candidate_id=candidate_id, tech_id=tech_id)
        else:
            return {
                       'status': 'fail',
                       'message': 'Unable to add a technology.'
                   }, 403

    @api.doc('delete technologies for a candidate', params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
    @token_required
    @api.response(200, 'Technologies successfully deleted.')
    def delete(self, tech_id):
        """Deleting technologies for a candidate"""
        if not isinstance(Auth.get_roles(request), str):
            candidate_id, _ = Auth.get_roles(request)
            if candidate_id:
                return delete_technologies(candidate_id=candidate_id, tech_id=tech_id)
        else:
            return {
                       'status': 'fail',
                       'message': 'Unable to delete a technology.'
                   }, 403


@api.route('/age/<age>')
class CandidateAge(Resource):
    @api.doc('get candidates by age', params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
    @admin_token_required
    @api.marshal_list_with(_candidate, mask='cid,email,name,surname,age,city,birth_year,technologies')
    def get(self, age):
        return search_candidate_by_age(age)
