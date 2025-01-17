from app import db


class Goal(db.Model):
    goal_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    tasks = db.relationship("Task", back_populates="goal")

    def dictionfy(self):
        return{
            "id":self.goal_id,
            "title":self.title}
    
    @classmethod
    def objectfy(cls,request_body):
        new_object = Goal(
            title=request_body['title']
        )
        return new_object