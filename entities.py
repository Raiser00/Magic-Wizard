import random

class Character:
    def __init__(self, name, healthMax):
        self.name = name
        self.healthMax = healthMax
        self.health = healthMax
        self.level = 1
        self.exp = 0
        self.position = [100, 100]
        self.deck = []

    def gainExp(self, amount):
        self.exp += amount
        if self.exp >= 100:
            self.level += 1
            self.exp = 0
            print(f"{self.name} monte au niveau {self.level}!")

class Card:
    def __init__(self, name, attack, defense):
        self.name = name
        self.atk = attack
        self.deff = defense
    def __str__(self):
        return f"{self.name} (ATK: {self.atk}, DEF: {self.deff})"
