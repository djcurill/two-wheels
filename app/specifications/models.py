from app import db


class Condition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(64), nullable=False, unique=True)

    def __repr__(self):
        return f"<Condition(value = {self.value})>"


class WheelSize(db.Model):
    __tablename__ = "wheel_size"
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(5), nullable=False, unique=True)

    def __repr__(self):
        return f"<WheelSize(value = {self.value})"


class FrameSize(db.Model):
    __tablename__ = "frame_size"
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(5), nullable=False, unique=True)

    def __repr__(self):
        return f"<FrameSize(value = {self.value})>"
