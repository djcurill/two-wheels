from app import db


class Bike(db.Model):
    __tablename__ = "bike"
    id = db.Column(db.Integer, primary_key=True)

    model_id = db.Column(db.Integer, db.ForeignKey("model.id"))
    model = db.relationship("Model", lazy="select")

    condition_id = db.Column(db.Integer, db.ForeignKey("condition.id"))
    condition = db.relationship("Condition", lazy="select")

    frame_size_id = db.Column(db.Integer, db.ForeignKey("frame_size.id"))
    frame_size = db.relationship("FrameSize", lazy="select")

    front_travel = db.Column(db.Float, default=0, nullable=False)
    rear_travel = db.Column(db.Float, default=0, nullable=False)
