import os

class Configuration:
    # Needed for a csrf token
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')
    FLASK_DEBUG = os.environ.get("FLASK_DEBUG")