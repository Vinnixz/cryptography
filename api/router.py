from flask import Flask
from api.routes.user import user_blueprint


def register_routes(app: Flask):
    app.register_blueprint(user_blueprint)
