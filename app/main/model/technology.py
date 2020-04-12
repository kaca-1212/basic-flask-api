from .. import db


class Technology(db.Model):
    """ Technology Model for storing user related details """
    __tablename__ = "technology"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Technology '{self.name}'>"
