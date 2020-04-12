from app.main import db
from app.main.model.candidate import Candidate
from app.main.model.candidate_shortlist import CandidateShortlist


def get_shortlist(admin_id):
    candidates_short_list = CandidateShortlist.query.filter_by(user_id=admin_id)
    candidates = Candidate.query.join(candidates_short_list).all()
    return candidates


def add_candidate_to_shortlist(candidate_id=None, user_id=None):
    new_candidate = CandidateShortlist(
        candidate_id=candidate_id,
        user_id=user_id
    )
    db.session.add(new_candidate)
    db.session.commit()


def delete_candidate_from_shortlist(candidate_id=None, user_id=None):
    db.session.delete(CandidateShortlist.query.filter_by(candidate_id=candidate_id).filter_by(user_id=user_id).first())
    db.session.commit()
