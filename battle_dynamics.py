from pakuri_moves import PakuriMoves
from pakuri import Pakuri

import pygame

class BattleDynamics():

    def __init__(self):
        self.multiplier = 1.0
        
        self.playerTurn = 1

        self.playerOnePakuri = None
        self.playerTwoPakuri = None

        self.speech = "Never Entered!!"
        self.dialogue = "Normal Power"

        self.abilityType = None
        self.doesDamage = None
        self.applyBuff = None
        self.applyDebuff = None
        self.selfHarm = None

        self.attackingPlayer = None

    def moveSelected(self, name, playerTurn, p1PakuriInstance, p2PakuriInstance):
        self.speech = "entered moveSelected"
        self.playerOnePakuri = p1PakuriInstance
        self.playerTwoPakuri = p2PakuriInstance

        self.playerTurn = playerTurn
        
        for i in range(len(PakuriMoves().moveDatabase)):
            self.speech = "hi"
            if name == PakuriMoves().moveDatabase[i][PakuriMoves().moveNameIndex]:
                self.moveName = name

                (self.abilityType, self.doesDamage, self.applyBuff, self.applyDebuff, self.selfHarm)\
                    = PakuriMoves().get_moveDetails(self.moveName)

                break

        self.moveEffects()

    def moveEffects(self):
        if self.doesDamage:
            self.speech = "entered does damage"
            self.determineMultiplier()
            self.damageCalculator()

        if self.applyBuff:

            if self.moveName == "Absorb" or "Growth" or "Moonlight" or "RCT" or "Za Warudo":
                self.speech = "entered applyBuff"
                if self.playerTurn == 1:
                    self.playerOnePakuri.increase_currentHealth()
                elif self.playerTurn == 2:
                    self.playerTwoPakuri.increase_currentHealth()

            if self.playerTurn == 1:
                self.playerOnePakuri.increaseAttack()
                self.playerTwoPakuri.increaseDefense()
            elif self.playerTurn == 2:
                self.playerTwoPakuri.increaseAttack()
                self.playerTwoPakuri.increaseDefense()

        if self.applyDebuff:

            if self.playerTurn == 2:
                self.speech = "entered applyDebuff"
                self.playerOnePakuri.decreaseAttack()
                self.playerTwoPakuri.decreaseDefense()
            elif self.playerTurn == 1:
                self.speech = "entered applyDebuff"
                self.playerTwoPakuri.decreaseAttack()
                self.playerTwoPakuri.decreaseDefense()

        if self.selfHarm:

            if self.playerTurn == 1:
                self.speech = "entered selfHarm"
                self.playerOnePakuri.decrease_currentHealth()
            elif self.playerTurn == 2:
                self.speech = "entered selfHarm"
                self.playerTwoPakuri.decrease_currentHealth()

    def damageCalculator(self):

        if(self.multiplier == 0.0):
            self.dialogue = "Move is Ineffective..."
        elif(self.multiplier == 1.5):
            self.dialogue = "Not Very Effective..."
        elif(self.multiplier == 2.0):
            self.dialogue = "Super Effective!"

        if self.playerTurn%2 != 0:
            if self.doesDamage == True and self.selfHarm == True:
                #pygame.draw.rect(self.screen, self.BLACK, (40, 650, 550, 200), 9)
                self.damage = int((((self.playerOnePakuri.get_attack()) / 10) + 7) * self.multiplier)
                self.playerTwoPakuri.takenDamage(self.damage)
            else:
                self.speech = ("Player One NOT self harm")
                self.damage = int((((self.playerOnePakuri.get_attack())/10) + 4) * self.multiplier)
                self.playerTwoPakuri.takenDamage(self.damage)

        else:

            if self.doesDamage == True and self.selfHarm == True:
                self.speech = ("Player Two IN self harm")
                self.damage = int((((self.playerTwoPakuri.get_attack()) / 10) + 7) * self.multiplier)
                self.playerOnePakuri.takenDamage(self.damage)
            else:
                self.speech = ("Player Two NOT self harm")
                self.damage = int((((self.playerTwoPakuri.get_attack())/10) + 4) * self.multiplier)
                self.playerOnePakuri.takenDamage(self.damage)

    def speechPrint(self):
        return self.speech

    def determineMultiplier(self):

        if self.playerTurn%2 != 0:
            self.typeDefender = self.playerTwoPakuri.get_type()
        else:
            self.typeDefender = self.playerOnePakuri.get_type()


        if self.abilityType == "Normal":
            if self.typeDefender == "Rock":
                self.multiplier = 0.5
            elif self.typeDefender == "Ghost":
                self.multiplier = 0.0
            elif self.typeDefender == "Steel":
                self.multiplier = 0.5

        elif self.abilityType == "Fire":
            if self.typeDefender == "Fire":
                self.multiplier = 0.5
            elif self.typeDefender == "Water":
                self.multiplier = 0.5
            elif self.typeDefender == "Grass":
                self.multiplier = 2.0
            elif self.typeDefender == "Ice":
                self.multiplier = 2.0
            elif self.typeDefender == "Bug":
                self.multiplier = 2.0
            elif self.typeDefender == "Rock":
                self.multiplier = 0.5
            elif self.typeDefender == "Dragon":
                self.multiplier = 0.5
            elif self.typeDefender == "Steel":
                self.multiplier = 2.0

        elif self.abilityType == "Water":
            if self.typeDefender == "Fire":
                self.multiplier = 2.0
            elif self.typeDefender == "Water":
                self.multiplier = 0.5
            elif self.typeDefender == "Grass":
                self.multiplier = 0.5
            elif self.typeDefender == "Ground":
                self.multiplier = 2.0
            elif self.typeDefender == "Rock":
                self.multiplier = 2.0
            elif self.typeDefender == "Dragon":
                self.multiplier = 0.5

        elif self.abilityType == "Electric":
            if self.typeDefender == "Water":
                self.multiplier = 2.0
            elif self.typeDefender == "Electric":
                self.multiplier = 0.5
            elif self.typeDefender == "Grass":
                self.multiplier = 0.5
            elif self.typeDefender == "Ground":
                self.multiplier = 0.0
            elif self.typeDefender == "Flying":
                self.multiplier = 2.0
            elif self.typeDefender == "Dragon":
                self.multiplier = 0.5

        elif self.abilityType == "Grass":
            if self.typeDefender == "Fire":
                self.multiplier = 0.5
            elif self.typeDefender == "Water":
                self.multiplier = 2.0
            elif self.typeDefender == "Grass":
                self.multiplier = 0.5
            elif self.typeDefender == "Poison":
                self.multiplier = 0.5
            elif self.typeDefender == "Ground":
                self.multiplier = 2.0
            elif self.typeDefender == "Flying":
                self.multiplier = 0.5
            elif self.typeDefender == "Dragon":
                self.multiplier = 0.5
            elif self.typeDefender == "Rock":
                self.multiplier = 2.0
            elif self.typeDefender == "Steel":
                self.multiplier = 0.5

        elif self.abilityType == "Fighting":
            if self.typeDefender == "Normal":
                self.multiplier = 2.0
            elif self.typeDefender == "Ice":
                self.multiplier = 2.0
            elif self.typeDefender == "Poison":
                self.multiplier = 0.5
            elif self.typeDefender == "Flying":
                self.multiplier = 0.5
            elif self.typeDefender == "Psychic":
                self.multiplier = 0.5
            elif self.typeDefender == "Bug":
                self.multiplier = 0.5
            elif self.typeDefender == "Rock":
                self.multiplier = 2.0
            elif self.typeDefender == "Ghost":
                self.multiplier = 0.0
            elif self.typeDefender == "Dark":
                self.multiplier = 2.0
            elif self.typeDefender == "Steel":
                self.multiplier = 2.0

        elif self.abilityType == "Ice":
            if self.typeDefender == "Fire":
                self.multiplier = 0.5
            elif self.typeDefender == "Water":
                self.multiplier = 0.5
            elif self.typeDefender == "Grass":
                self.multiplier = 2.0
            elif self.typeDefender == "Ice":
                self.multiplier = 0.5
            elif self.typeDefender == "Ground":
                self.multiplier = 0.5
            elif self.typeDefender == "Bug":
                self.multiplier = 2.0
            elif self.typeDefender == "Flying":
                self.multiplier = 2.0
            elif self.typeDefender == "Dragon":
                self.multiplier = 2.0
            elif self.typeDefender == "Steel":
                self.multiplier = 0.5

        elif self.abilityType == "Poison":
            if self.typeDefender == "Grass":
                self.multiplier = 2.0
            elif self.typeDefender == "Poison":
                self.multiplier = 0.5
            elif self.typeDefender == "Ground":
                self.multiplier = 0.5
            elif self.typeDefender == "Rock":
                self.multiplier = 0.5
            elif self.typeDefender == "Ghost":
                self.multiplier = 0.5
            elif self.typeDefender == "Steel":
                self.multiplier = 0.0

        elif self.abilityType == "Ground":
            if self.typeDefender == "Fire":
                self.multiplier = 2.0
            elif self.typeDefender == "Electric":
                self.multiplier = 2.0
            elif self.typeDefender == "Grass":
                self.multiplier = 0.5
            elif self.typeDefender == "Poison":
                self.multiplier = 2.0
            elif self.typeDefender == "Rock":
                self.multiplier = 2.0
            elif self.typeDefender == "Bug":
                self.multiplier = 0.5
            elif self.typeDefender == "Flying":
                self.multiplier = 0.0
            elif self.typeDefender == "Steel":
                self.multiplier = 2.0

        elif self.abilityType == "Flying":
            if self.typeDefender == "Electric":
                self.multiplier = 0.5
            elif self.typeDefender == "Grass":
                self.multiplier = 2.0
            elif self.typeDefender == "Fighting":
                self.multiplier = 2.0
            elif self.typeDefender == "Bug":
                self.multiplier = 2.0
            elif self.typeDefender == "Rock":
                self.multiplier = 0.5
            elif self.typeDefender == "Steel":
                self.multiplier = 0.5

        elif self.abilityType == "Psychic":
            if self.typeDefender == "Fighting":
                self.multiplier = 2.0
            elif self.typeDefender == "Poison":
                self.multiplier = 2.0
            elif self.typeDefender == "Psychic":
                self.multiplier = 0.5
            elif self.typeDefender == "Dark":
                self.multiplier = 0.0
            elif self.typeDefender == "Steel":
                self.multiplier = 0.5

        elif self.abilityType == "Bug":
            if self.typeDefender == "Fire":
                self.multiplier = 0.5
            elif self.typeDefender == "Grass":
                self.multiplier = 2.0
            elif self.typeDefender == "Fighting":
                self.multiplier = 0.5
            elif self.typeDefender == "Poison":
                self.multiplier = 0.5
            elif self.typeDefender == "Flying":
                self.multiplier = 0.5
            elif self.typeDefender == "Psychic":
                self.multiplier = 2.0
            elif self.typeDefender == "Ghost":
                self.multiplier = 0.5
            elif self.typeDefender == "Dark":
                self.multiplier = 2.0
            elif self.typeDefender == "Steel":
                self.multiplier = 0.5

        elif self.abilityType == "Rock":
            if self.typeDefender == "Fire":
                self.multiplier = 2.0
            elif self.typeDefender == "Ice":
                self.multiplier = 2.0
            elif self.typeDefender == "Fighting":
                self.multiplier = 0.5
            elif self.typeDefender == "Ground":
                self.multiplier = 0.5
            elif self.typeDefender == "Flying":
                self.multiplier = 2.0
            elif self.typeDefender == "Bug":
                self.multiplier = 2.0
            elif self.typeDefender == "Steel":
                self.multiplier = 0.5

        elif self.abilityType == "Ghost":
            if self.typeDefender == "Normal":
                self.multiplier = 0.0
            elif self.typeDefender == "Psychic":
                self.multiplier = 2.0
            elif self.typeDefender == "Ghost":
                self.multiplier = 2.0
            elif self.typeDefender == "Dark":
                self.multiplier = 0.5

        elif self.abilityType == "Dragon":
            if self.typeDefender == "Dragon":
                self.multiplier = 2.0
            elif self.typeDefender == "Steel":
                self.multiplier = 0.5

        elif self.abilityType == "Dark":
            if self.typeDefender == "Fighting":
                self.multiplier = 0.5
            elif self.typeDefender == "Psychic":
                self.multiplier = 2.0
            elif self.typeDefender == "Ghost":
                self.multiplier = 2.0
            elif self.typeDefender == "Dark":
                self.multiplier = 0.5

        elif self.abilityType == "Steel":
            if self.typeDefender == "Fire":
                self.multiplier = 0.5
            elif self.typeDefender == "Water":
                self.multiplier = 0.5
            elif self.typeDefender == "Grass":
                self.multiplier = 0.5
            elif self.typeDefender == "Ice":
                self.multiplier = 2.0
            elif self.typeDefender == "Rock":
                self.multiplier = 2.0
            elif self.typeDefender == "Steel":
                self.multiplier = 0.5

        elif self.abilityType == "Fairy":
            if self.typeDefender == "Fire":
                self.multiplier = 0.5
            elif self.typeDefender == "Fighting":
                self.multiplier = 2.0
            elif self.typeDefender == "Posison":
                self.multiplier = 0.5
            elif self.typeDefender == "Dark":
                self.multiplier = 2.0
            if self.typeDefender == "Dragon":
                self.multiplier = 2.0
            elif self.typeDefender == "Steel":
                self.multiplier = 0.5

    def attackEffectiveness(self):
        return self.dialogue