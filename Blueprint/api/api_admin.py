from flask import Blueprint, jsonify

apiAdmin = Blueprint("apiAdmin", __name__, url_prefix="/api/admin")

@apiAdmin.route("/")
def index():
    return jsonify({
        "success": True,
        "message": "Hello Admin!",
        })
