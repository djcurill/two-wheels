from app import db, ma


class Condition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(64), nullable=False, unique=True)

    def __repr__(self):
        return f"<Condition(value = {self.value})>"


class ConditionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Condition

    id = ma.auto_field()
    value = ma.auto_field()


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


class Brand(db.Model):
    __tablename__ = "brand"
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
        return f"<Brand(value = {self.value})>"


class Model(db.Model):
    __tablename__ = "model"
    id = db.Column(db.Integer, primary_key=True)
    brand_id = db.Column(db.Integer, db.ForeignKey("brand.id"), nullable=False)
    brand = db.relationship("Brand", lazy=True)
    value = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Model(brand_id = {self.brand_id}, value = {self.value})>"
