from flask import Flask
from flask_login import LoginManager

from app.routes import items, pokemon
import os
from app.config import Configuration
# import statement for CSRF
from flask_wtf.csrf import CSRFProtect, generate_csrf

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(items.bp)
app.register_blueprint(pokemon.bp)


@app.route("/")
def index():
    return "<h1> Happy Happy Joy Joy </h1>"

# after request code for CSRF token injection
@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response
