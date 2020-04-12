from .. import db
from .candidate import Candidate
from .technology import Technology


class Candidate_Tech(db.Model):
    __tablename__ = 'candidate_tech'

    id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.cid'))
    tech_id = db.Column(db.Integer, db.ForeignKey('technology.id'))

    candidate = db.relationship(Candidate, backref=db.backref("candidate_tech", cascade="all, delete-orphan"))
    technology = db.relationship(Technology, backref=db.backref("candidate_tech", cascade="all, delete-orphan"))
