import random

class Character:
    def __init__(self, name, healthMax):
        self.name = name
        self.healthMax = healthMax
        self.health = healthMax
        self.level = 1
        self.exp = 0
        self.position = [100, 100]
        self.emptyCard = 5
        self.deck = []
        self.ActiveCard = None

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

class Monster:
    def __init__(self, name, baseAtk, baseDeff, baseRank, actualLevel=1):
        self.name = name
        self.baseAtk = baseAtk
        self.baseDeff = baseDeff
        self.baseRank = baseRank
        self.actualLevel = actualLevel

        self.healthMax = baseRank * 100
        self.health = self.healthMax


    @property
    def atk(self):
        value = (self.baseAtk / self.baseRank) * self.actualLevel
        return int(value)

    @property
    def deff(self):
        value = (self.baseDeff / self.baseRank) * self.actualLevel
        return int(value)
    
    def __str__(self):
        return f"{self.name} (Niv.{self.actualLevel}/{self.baseRank}) ATK:{self.atk} DEF:{self.deff}"