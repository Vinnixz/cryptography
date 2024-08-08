import pdb
import bcrypt
from flask import jsonify, Response
from database.user import UserDB

class UserController:
    def __init__(self, dao: UserDB):
        self._dao = dao

    def create_user(self, document: str, credit_card: str) -> Response:
       # hashed_document = bcrypt.hashpw(document.encode("utf-8"), bcrypt.gensalt()).decode('utf-8')
        #hashed_credit_card = bcrypt.hashpw(credit_card.encode("utf-8"), bcrypt.gensalt()).decode('utf-8')
        result = self._dao.create_user(document, credit_card)
        if result:
            return jsonify({"msg": "Usuário registrado"}), 201
        return jsonify({"msg": "Problema ao registrar usuário"}), 400
