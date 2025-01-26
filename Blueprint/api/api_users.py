from flask import Blueprint, jsonify

apiUsers = Blueprint("apiUsers", __name__, url_prefix="/api/users")

@apiUsers.route("/")
def index():
    return jsonify({
        "success": True,
        "message": "Hello Users!",
        })

@apiUsers.route("/<int:id>")
def getById(id):
    return jsonify({
        "success": True,
        "message": f"User with id {id}",
        })
