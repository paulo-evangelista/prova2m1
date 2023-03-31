from orm import db, Game

response = db.query(Game).all()
for i in response:
    print("\n\n ->", i)