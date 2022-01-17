from app.specifications import bp
from app.specifications.models import Condition, ConditionSchema
from flask import jsonify

conditions_schema = ConditionSchema(many=True)


@bp.route("/")
def get_conditions():
    conditions = Condition.query.all()
    return jsonify(conditions_schema.dump(conditions))
