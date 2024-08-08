from api.app import app
from database.database import create_table

def main():
    app.run(host="0.0.0.0", port=8000, debug=True)

if __name__=="__main__":
    create_table()
    main()