from random_app.urls import app
from random_app.models import db
from load_env_config import PORT, HOST




if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(port=PORT, host=HOST, debug=False)