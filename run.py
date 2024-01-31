from random_app.urls import app
from random_app.models import db




if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(port=8080)