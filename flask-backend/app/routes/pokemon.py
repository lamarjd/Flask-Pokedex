from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user, login_required



bp = Blueprint('pokemon', __name__, url_prefix="/pokemon")

@bp.route('/', methods=["GET", "POST"])
def index():
  return "<h1>Some Pokemon </h1>"


@bp.route('/<int:id>')
def main():
  return "<h1>hello</h1>"
