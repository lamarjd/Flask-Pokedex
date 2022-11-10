from app.models import db, Pokemon, Item
from app import app

print("I'm the seeder data")


with app.app_context():
    
    # db.drop_all()
    # print("All tables dropped!")

    # db.create_all()
    # print("Create all tables!")

    pokemon1 = Pokemon(
        number=1,
        imageUrl='/images/pokemon_snaps/1.svg',
        name='Bulbasaur',
        attack=49,
        defense=49,
        type='grass',
        moves="tackle",
        captured=True
    )

    pokemon2 = Pokemon(
        number=2,
        imageUrl='/images/pokemon_snaps/2.svg',
        name='Blastoise',
        attack=49,
        defense=49,
        type='water',
        moves="surf",
        captured=True
    )

    pokemon3 = Pokemon(
        number=3,
        imageUrl='/images/pokemon_snaps/3.svg',
        name='Charizard',
        attack=62,
        defense=63,
        type='fire',
        moves="scortch",
        captured=True
    )

   
    
    pokemons = [pokemon1, pokemon2, pokemon3]
    for pokemon in pokemons:
        db.session.add(pokemon)

    db.session.commit()
    print("All pokemon created!")