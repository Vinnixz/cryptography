from api.app import app
import api.router
from database.database import DatabaseManager


def main():
    api.router.register_routes(app)
    app.run(host="0.0.0.0", port=8000, debug=True)


if __name__ == "__main__":
    DatabaseManager.initialize("sqlite:///database.db")
    DatabaseManager.migrate()
    main()
