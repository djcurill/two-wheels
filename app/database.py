from app import db
from app.specifications.models import Brand, Condition, FrameSize, WheelSize
from app.constants import brands, frame_sizes, conditions, wheel_sizes


def wipe_db():
    db.drop_all()


def init_db():
    db.create_all()

    condition_models = [Condition(value=val) for val in conditions]
    db.session.add_all(condition_models)

    frame_size_models = [FrameSize(value=val) for val in frame_sizes]
    db.session.add_all(frame_size_models)

    wheel_size_models = [WheelSize(value=val) for val in wheel_sizes]
    db.session.add_all(wheel_size_models)

    brand_models = [Brand(value=val) for val in brands]
    db.session.add_all(brand_models)
    db.session.commit()
