from app.specifications import bp


@bp.route("/")
def get_conditions():
    return "Testing"
