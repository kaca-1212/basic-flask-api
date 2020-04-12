from werkzeug.utils import cached_property
from flask_restplus import Namespace, fields


class TechnologyDto:
    api = Namespace('technology', description='technology related description')
    technology = api.model('technology', {
        'name': fields.String(required=True, desription='technology name'),
        'id': fields.Integer(required=False, description='technology id')
    })


class CandidateDto:
    api = Namespace('candidate', description='candidate related operations')
    candidate = api.model('candidate', {
        'cid': fields.Integer(required=False, description='candidate id'),
        'name': fields.String(required=True, description='candidate name'),
        'surname': fields.String(required=True, description='candidate surname'),
        'city': fields.String(required=True, description='candidate city'),
        'birth_year': fields.String(required=True, description='candidate birth year'),
        'email': fields.String(required=True, description='candidate email'),
        'password': fields.String(required=True, description='candidate password'),
        'technologies': fields.List(fields.Nested(TechnologyDto.technology), required=True,
                                    description='candidate technologies')
    })


class ShortlistDto:
    api = Namespace('shortlist', description='operations related to shortlist of candidates')


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user password'),
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })
