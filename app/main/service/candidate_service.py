import datetime

from app.main import db
from app.main.model.candidate import Candidate
from app.main.model.candidate_tech import Candidate_Tech
from app.main.model.technology import Technology
from .user_service import generate_token


def save_new_candidate(data):
    candidate = Candidate.query.filter_by(email=data['email']).first()
    if candidate:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please log in.',
        }
        return response_object, 409

    new_candidate = Candidate(
        email=data['email'],
        password=data['password'],
        registered_on=datetime.datetime.utcnow(),
        name=data['name'],
        surname=data['surname'],
        city=data['city'],
        birth_year=data['birth_year']
    )
    if len(data['technologies']) == 0:
        response_object = {
            'status': 'fail',
            'message': "At least one technology required",
        }
        return response_object, 409

    for tech in data['technologies']:
        new_tech = Technology.query.filter_by(id=tech['id']).first()
        if not new_tech:
            response_object = {
                'status': 'fail',
                'message': "Technology doesn't exist.",
            }
            return response_object, 409

        new_candidate.technologies.append(new_tech)
    db.session.add(new_candidate)

    db.session.commit()
    return generate_token(new_candidate)


def delete_candidate(candidate_id):
    db.session.delete(Candidate.query.filter_by(id=candidate_id).first())
    db.session.commit()


def search_candidate_by_age(age):
    current_year = datetime.datetime.now().year
    required_birth_year = current_year - int(age)
    candidates = Candidate.query.filter_by(birth_year=required_birth_year).all()
    if not candidates:
        response_object = {
            'status': 'fail',
            'message': "Candidate not found.",
        }
        return response_object, 404
    else:
        return candidates


def search_candidates_by_tech(tech_id):
    candidates = Candidate.query.join(Candidate_Tech).filter_by(tech_id=tech_id).all()
    if not candidates:
        response_object = {
            'status': 'fail',
            'message': "Candidate not found.",
        }
        return response_object, 404
    else:
        return candidates


def add_technologies(tech_id=None, candidate_id=None):
    can_tech = Candidate_Tech(
        candidate_id=candidate_id,
        tech_id=tech_id
    )
    db.session.add(can_tech)
    db.session.commit()
    return {
               'status': 'success',
               'message': 'Technology successfully added.'
           }, 201


def delete_technologies(tech_id=None, candidate_id=None):
    response_object = {
        'status': 'fail',
        'message': "Candidate doesn't have this technology.",
    }

    can_tech = Candidate_Tech.query.filter_by(candidate_id=candidate_id).filter_by(tech_id=tech_id).first()
    if not can_tech:
        response_object.update({'message': 'Technology is not linked to user'})
        return response_object, 409

    if len(Candidate_Tech.query.filter_by(candidate_id=candidate_id).all()) == 1:
        response_object.update({'message': "Candidate must have at least one technology."})
        return response_object, 409
    else:
        db.session.delete(Candidate_Tech.query.filter_by(candidate_id=candidate_id).filter_by(tech_id=tech_id).first())
        db.session.commit()
        return {
                   'status': 'success',
                   'message': 'Technology successfully deleted.'
               }, 201


def get_all_candidates():
    candidates = Candidate.query.all()
    return candidates
