from .. import db
from .candidate import Candidate


class CandidateShortlist(db.Model):
    __tablename__ = 'candidate_shortlist'

    id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.cid'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    candidate = db.relationship(Candidate, foreign_keys=[candidate_id],
                                backref=db.backref("candidate_shortlist", cascade="all, delete-orphan"))
