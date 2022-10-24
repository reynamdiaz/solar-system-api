from flask import Blueprint

class Planet:

    def __init__(self, id, name, description, moons):
        self.id = id
        self.name = name
        self.description = description
        self.moons = moons

planets = [
    Planet(1, "Earth", "our home", 1),
    Planet(2, "Mars", "red planet", 2),
    Planet(3, "Pluto", "is a planet", 5)
]
