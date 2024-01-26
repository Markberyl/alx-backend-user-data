from flask import Flask, jsonify
from api.v1.views import index

app = Flask(__name__)
app.register_blueprint(index.app_views)

# Add a new error handler for status code 401
@app.errorhandler(401)
def unauthorized_error(error):
    response = jsonify({"error": "Unauthorized"})
    response.status_code = 401
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

