from models import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    client_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)    
    client_request = db.Column(db.Text)

    user = db.relationship('User', foreign_keys=[user_id], backref='consultant_projects')
    client = db.relationship('User', foreign_keys=[client_id], backref='client_projects')

    def __repr__(self):
        return f'<Project {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'client_id': self.client_id,
            'client': self.client.to_dict() if self.client else None,
            'user_id': self.user_id,
            'user': self.user.to_dict() if self.user else None,
            'client_request': self.client_request
        }
