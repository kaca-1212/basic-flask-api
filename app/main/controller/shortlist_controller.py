from flask import request
from flask_restplus import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import CandidateDto, ShortlistDto
from ..service.shortlist_service import get_shortlist, add_candidate_to_shortlist, delete_candidate_from_shortlist
from ..service.auth_helper import Auth

api = ShortlistDto.api
_candidate = CandidateDto.candidate


@api.route('/candidate/')
class CandidateShortlist(Resource):
    @api.doc('Get shortlist of candidates', params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
    @admin_token_required
    @api.marshal_list_with(_candidate, mask='cid,email,name,surname,age,city,birth_year,technologies')
    def get(self):
        if not isinstance(Auth.get_roles(request), str):
            _, admin_id = Auth.get_roles(request)

            return get_shortlist(admin_id)
        else:
            return {
                       'status': 'fail',
                       'message': 'Unable to get shortlist of canidates.'
                   }, 404


@api.route('/candidate/<candidate_id>')
class CandidateShortlistSpec(Resource):
    @api.expect(_candidate, validate=True)
    @api.doc('Adding candidate to the shortlist', params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
    @admin_token_required
    def post(self, candidate_id):
        if not isinstance(Auth.get_roles(request), str):
            _, admin_id = Auth.get_roles(request)
            if candidate_id:
                return add_candidate_to_shortlist(candidate_id=candidate_id, user_id=admin_id)
        else:
            return {
                       'status': 'fail',
                       'message': 'Unable to add a candidate to shortlist.'
                   }, 403

    @api.doc('deleting candidate from the shortlist', params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
    @admin_token_required
    def delete(self, candidate_id):
        if not isinstance(Auth.get_roles(request), str):
            _, user_id = Auth.get_roles(request)
            if candidate_id:
                return delete_candidate_from_shortlist(candidate_id=candidate_id, user_id=user_id)
        else:
            return {
                       'status': 'fail',
                       'message': 'Unable to add a technology.'
                   }, 403
