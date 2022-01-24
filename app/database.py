from app import db
from app.specifications.models import Brand, Condition, FrameSize, WheelSize
from app.constants import brands, frame_sizes, conditions


def wipe_db():
    db.drop_all()


def init_db():
    db.create_all()

    conditions = [Condition(value=val) for val in conditions]
    db.session.add_all(conditions)

    frame_sizes = [FrameSize(value=val) for val in frame_sizes]
    db.session.add_all(frame_sizes)

    wheel_sizes = ["27.5", "29"]
    wheel_sizes = [WheelSize(value=val) for val in wheel_sizes]
    db.session.add_all(wheel_sizes)

    brands = [Brand(value=val) for val in brands]
    db.session.add_all(brands)
    db.session.commit()
