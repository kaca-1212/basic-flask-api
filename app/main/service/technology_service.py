from sqlalchemy import func
from app.main import db
from app.main.model.technology import Technology
from app.main.model.candidate_tech import Candidate_Tech
from app.main.model.candidate import Candidate


def save_new_technology(data):
    tech = Technology.query.filter_by(name=data['name']).first()
    if not tech:
        new_tech = Technology(
            name=data['name']
        )
        db.session.add(new_tech)
        db.session.commit()
        return new_tech
    else:
        response_object = {
            'status': 'fail',
            'message': 'This technology already exist in the database.',
        }
        return response_object, 409


def delete_a_technology(data):
    tech = Technology.query.filter_by(id=data['id']).first()
    if tech:
        for can_tech in Candidate_Tech.query.filter_by(tech_id=data['id']).all():
            if Candidate_Tech.query.with_entities(Candidate_Tech.candidate_id,
                                                  func.count(Candidate_Tech.tech_id)).group_by(
                Candidate_Tech.candidate_id).filter_by(tech_id=can_tech.tech_id).first()[1] == 1:
                db.session.delete(Candidate.query.filter_by(cid=can_tech.candidate_id).first())
        db.session.delete(tech)
        db.session.commit()
        return {
                   'status': 'success',
                   'message': 'Technology successfully deleted.'
               }, 200
    else:
        response_object = {
            'status': 'fail',
            'message': "This technology doesn't exist in the database.",
        }
        return response_object, 404


def get_all_technologies():
    return Technology.query.all()
