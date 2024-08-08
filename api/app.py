from flask import Flask, request
from controller.user import UserController
from database.user import UserDB

dao = UserDB
app = Flask(__name__)
user_controller = UserController(dao)

@app.route("/alive")
def alive():
    return "<h1>LIVE</h1>"

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    document = data.get("document")
    credit_card = data.get("credit_card")

    response, status_code = user_controller.create_user(document, credit_card)
    return response, status_code