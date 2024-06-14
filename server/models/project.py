from models import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    consultant_id = db.Column(db.Integer, db.ForeignKey('consultant.id'), nullable=False)
    client_request = db.Column(db.Text)

    consultant = db.relationship('Consultant', foreign_keys=[consultant_id], backref='consultant_projects')
    client = db.relationship('Client', foreign_keys=[client_id], backref='client_projects')

    def __repr__(self):
        return f'<Project {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'client_id': self.client_id,
            'client': self.client.to_dict() if self.client else None,
            'consultant_id': self.consultant_id,
            'consultant': self.consultant.to_dict() if self.consultant else None,
            'client_request': self.client_request
        }
