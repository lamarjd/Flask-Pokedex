from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user, login_required



bp = Blueprint("items", __name__, url_prefix="/items")


@bp.route("/", methods=["GET", "PUT", "DELETE"])
def update_item():
  return "<h1> I HATE MY LIFE </h1>"
