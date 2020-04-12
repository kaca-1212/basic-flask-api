from .. import db
from .user import User
from .technology import Technology


class Candidate(User):
    """ Candidate Model for storing candidate related details """
    __tablename__ = "candidate"

    __mapper_args__ = {
        'polymorphic_identity': 'candidate',
    }

    cid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    birth_year = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(f"{User.__tablename__}.id"))
    technologies = db.relationship(Technology, secondary='candidate_tech')

    def __repr__(self):
        return f"<Candidate '{self.name} {self.surname}'>"
