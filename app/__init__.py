from flask_restplus import Api
from flask import Blueprint
from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.candidate_controller import api as candidate_ns
from .main.controller.technology_controller import api as technology_ns
from .main.controller.shortlist_controller import api as shortlist_ns

blueprint = Blueprint('api', __name__)

authorizations = {
    'token': {
        'type': 'bearer',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(blueprint,
          authorizations=authorizations,
          title='Basic API',
          version='1.0',
          description='API for managing the canidates'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(candidate_ns, path='/candidate')
api.add_namespace(technology_ns, path='/technology')
api.add_namespace(shortlist_ns, path='/shortlist')
