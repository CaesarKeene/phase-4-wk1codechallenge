from flask import Flask
from models import db, Power, Hero, HeroPower
from random import choice

def seed_powers():
    print("🦸‍♀ Seeding powers...")
    powers = [
        Power(name="Strength", description="Super strength"),
        Power(name="Being Rich", description="Wealth"),
        Power(name="Telekinesis", description="Move objects with the mind"),
        
    ]

    db.session.add_all(powers)
    db.session.commit()
    print("🦸‍♀ Powers seeded!")

def seed_heroes():
    print("🦸‍♀ Seeding heroes...")
    heroes = [
        Hero(name="Hulk", super_name="Bruce Banner"),
        Hero(name="Batman", super_name="Bruce Wayne"),
        Hero(name="Spider-Man", super_name="Peter Parker"),
        
    ]

    db.session.add_all(heroes)
    db.session.commit()
    print("🦸‍♀ Heroes seeded!")

def seed_hero_powers():
    print("🦸‍♀ Adding powers to heroes...")
    strengths = ["Strong", "Weak", "Average"]
    heroes = Hero.query.all()

    for hero in heroes:
        for _ in range(choice([1, 2, 3])):
            power = Power.query.order_by(db.func.random()).first()
            hero_power = HeroPower(hero=hero, power=power, strength=choice(strengths))
            db.session.add(hero_power)

    db.session.commit()
    print("🦸‍♀ Done seeding!")

if __name__ == '__main__':
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()
        seed_powers()
        seed_heroes()
        seed_hero_powers()
