from orm import db, Game

lista_jogos = [
    Game(name="DEAD SPACE REMAKE",console="PS5",price=350,quantity=8),
    Game(name=" FORSPOKEN",console="PC",price=299,quantity=8),
    Game(name="DEAD ISLAND 2",console="PS5",price=350,quantity=10),
    Game(name="HOGWARTS LEGACY",console="PC",price=219,quantity=7),
    Game(name="WILD HEARTS",console="XBox Series",price=350,quantity=7),
    Game(name="RESIDENT EVIL 4",console="PS5",price=289,quantity=10),
    Game(name="THE LEGEND OF ZELDA: TEARS OF THE KINGDOM",console="Switch",price=350,quantity=10),
]

db.add_all(lista_jogos)
db.commit()