from flask import Blueprint, redirect, render_template, url_for, jsonify
from flask_login import current_user, login_required

from app.models import Pokemon



bp = Blueprint('pokemon', __name__, url_prefix="/api")

@bp.route('/pokemon', methods=["GET", "POST"])
def index():
  list = Pokemon.query.all()
  print(list)
  dict = [i.__dict__ for i in list]
  for i in dict:
    del i['_sa_instance_state']

  return jsonify(dict)
  
  

  









@bp.route('/<int:id>', methods=["GET", "PUT"])
def main(id):
  ###
  # GET QUERY pokomen = Pokemon.query.get(id)
  #  PUT, query pokemon, do some shit, return
  return f"<h1>Hello number {id}</h1>"

@bp.route("/<int:id>/items", methods=["GET", "POST"])
def items(id):
  return f"This boy number {id} got some items"

@bp.route("/types")
def types():
  return "<h1>GOT DEM TYPES</h1>"

@bp.route("/random")
def random():
  return "<h1>Holy shit that's so random</h1>"

@bp.route("/battle")
def battle():
  return "<h1> IT'S TIME TO DUEL BITCH</h1>"
