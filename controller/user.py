import bcrypt
from flask import jsonify, Response
from database.models.user import User


class UserController:
    def __init__(self, session):
        self.session = session

    def create_user(self, document: str, credit_card: str) -> Response:
        try:
            hashed_document = bcrypt.hashpw(
                document.encode("utf-8"), bcrypt.gensalt()
            ).decode("utf-8")
            hashed_credit_card = bcrypt.hashpw(
                credit_card.encode("utf-8"), bcrypt.gensalt()
            ).decode("utf-8")
            new_user = User(document=hashed_document, credit_card=hashed_credit_card)
            self.session.add(new_user)
            self.session.commit()
            return jsonify({"msg": "Usuário registrado"}), 201
        except Exception as e:
            self.session.rollback()
            return jsonify({"msg": "Problema ao registrar usuário"}), 400
