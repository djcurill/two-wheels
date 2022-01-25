from app import db
from app.specifications.models import Brand, Condition, FrameSize, WheelSize, Model
from app.constants import bikes, frame_sizes, conditions, wheel_sizes


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

    brands = sorted(list(bikes.keys()))
    brand_models = [Brand(id=i, value=val) for i, val in enumerate(brands)]
    db.session.add_all(brand_models)

    bike_models = []
    for brand in brand_models:
        for model in bikes[brand.value]:
            bike_models.append(Model(brand_id=brand.id, value=model))

    db.session.add_all(bike_models)
    db.session.commit()
