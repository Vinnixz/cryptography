from flask import Blueprint, request, jsonify
from controller.user import UserController
from database.database import DatabaseManager

DatabaseManager.initialize("sqlite:///database.db")
session = DatabaseManager.Session()

user_blueprint = Blueprint("user", __name__)

user_controller = UserController(session)


@user_blueprint.route("/alive")
def alive():
    return "<h1>LIVE</h1>"


@user_blueprint.route("/register", methods=["POST"])
def register():
    data = request.json
    document = data.get("document")
    credit_card = data.get("credit_card")

    if not document or not credit_card:
        return jsonify({"msg": "Dados incompletos"}), 400

    response, status_code = user_controller.create_user(document, credit_card)
    return response, status_code
