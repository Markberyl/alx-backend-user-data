from flask import Blueprint, abort

app_views = Blueprint("app_views", __name__)

# Add a new endpoint that raises a 401 error using abort
@app_views.route("/api/v1/unauthorized", methods=["GET"])
def unauthorized_endpoint():
    abort(401)


