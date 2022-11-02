from app import db
from datetime import datetime


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    completed_at = db.Column(db.DateTime, default=None, nullable=True)

    def dictionfy(self):
        return{
            "id":self.task_id,
            "title":self.title,
            "description":self.description,
            "is_complete": True if self.completed_at is not None else False
        }