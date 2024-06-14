from models import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('consultant.id'), nullable=False)
    user = db.relationship('Consultant', backref='posts')

    def __repr__(self):
        return f'<Post {self.title}>'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'user_id': self.user_id,
            'user': self.user.to_dict() if self.user else None
        }