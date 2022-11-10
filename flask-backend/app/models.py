from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()


class Pokemon(db.Model):
    __tablename__ = 'pokemons'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False, unique=True)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    imageUrl= db.Column(db.String(255), nullable=False)
    name= db.Column(db.String(255), nullable=False, unique=True)
    type = db.Column(db.String(255), nullable=False)
    moves = db.Column(db.String(255), nullable=False)
    encounterRate = db.Column(db.Float, default=1.00, nullable=False)
    catchRate = db.Column(db.Float, default=1.00, nullable=False)
    captured = db.Column(db.Boolean, nullable=False)
    createdAt = db.Column(db.DateTime)
    updatedAt = db.Column(db.DateTime)

class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    happiness = db.Column(db.Integer, nullable=False)
    imageUrl = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    pokemonId = db.Column(db.Integer, db.ForeignKey('pokemons.id'), nullable=False)

    createdAt = db.Column(db.DateTime, nullable=False)
    updatedAt = db.Column(db.DateTime, nullable=False)


    