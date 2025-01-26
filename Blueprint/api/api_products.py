from flask import Blueprint, jsonify

apiProducts = Blueprint("apiProducts", __name__, url_prefix="/api/products")

@apiProducts.route("/")
def index():
    return jsonify({
        "success": True,
        "message": "Hello Products!",
        })

@apiProducts.route("/<int:id>")
def getById(id):
    return jsonify({
        "success": True,
        "message": f"Product with id {id}",
        })
