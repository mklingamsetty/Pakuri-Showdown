class Pakuri:
    def __init__(self, species):

        self.species = species
        self.attack = (len(species) * 7) + 9
        self.defense = (len(species) * 5) + 17
        self.speed = (len(species) * 6) + 13
        self.health = (len(species) * 10) + 11

        if self.species == "Flamix":
            self.type = ["Fire"]
            self.moveset = ["Ember", "Scratch", "Growl", "Agility"]
        elif self.species == "Aquoray":
            self.type = ["Water", "Electric"]
            self.moveset = ["Aqua Jet", "Buzz", "Block", "Charge"]
        elif self.species == "Terrasaur":
            self.type = ["Flying", "Dark"]
            self.moveset = ["Crunch", "Crush Claw", "Gust", "Drill Peck"]
        elif self.species == "Electrixie":
            self.type = ["Electric"]
            self.moveset = ["Electro Ball", "Scratch", "Sword Dance", "Electro Web"]
        elif self.species == "Windora":
            self.type = ["Water", "Ghost"]
            self.moveset = ["Bubble Beam", "Astonish", "Astral Barrage", "Life Dew"]
        elif self.species == "Glaciorb":
            self.type = ["Ice", "Fairy"]
            self.moveset = ["Ice Shard", "Icy Wind", "Light of Ruin", "Moonlight"]
        elif self.species == "Pyrotusk":
            self.type = ["Fire", "Rock"]
            self.moveset = ["Flamethrower", "Fire Kick", "Rock Blast", "Fortify"]
        elif self.species == "Leaflynx":
            self.type = ["Grass", "Fairy"]
            self.moveset = ["Absorb", "Bite", "Vine Whip", "Misty Explosion"]
        elif self.species == "Magmawisp":
            self.type = ["Ghost", "Fire"]
            self.moveset = ["Moongeist Beam", "Rage Fist", "Sacred Fire", "Will-O-Wisp"]
        elif self.species == "Thundragon":
            self.type = ["Electric", "Dragon"]
            self.moveset = ["Wild Charge", "Zap Cannon", "Ascend", "Dragon Breath"]
        elif self.species == "Frostbite":
            self.type = ["Ice", "Psychic"]
            self.moveset = ["Zen Headbutt", "Reflect", "Mist", "Ice Ball"]
        elif self.species == "Rockscale":
            self.type = ["Ground", "Posion"]
            self.moveset = ["Mud Bomb", "Dig", "Toxic", "Poison Jab"]
        elif self.species == "Volcanix":
            self.type = ["Bug", "Fighting"]
            self.moveset = ["Bug Bite", "Agility", "Mega Punch", "Pump Up"]
        elif self.species == "Aquaflare":
            self.type = ["Water", "Dragon"]
            self.moveset = ["Hydropump", "Soul Buff", "Draco Meteor", "Razor Shell"]
        elif self.species == "Zephyria":
            self.type = ["Dark", "Ghost"]
            self.moveset = ["Crunch", "Haunt", "Cleave", "Frighten"]
        elif self.species == "Leafstorm":
            self.type = ["Grass", "Flying"]
            self.moveset = ["Seed Bomb", "Blitz", "Agility", "Growth"]
        elif self.species == "Thunderclaw":
            self.type = ["Electric", "Flying"]
            self.moveset = ["Lightning Bolt", "Gust", "Agility", "Scratch"]
        elif self.species == "Endorphine":
            self.type = ["Psychic", "Dark"]
            self.moveset = ["Psywave", "Shadow Punch", "Za Warudo", "Emerald Splash"]
        elif self.species == "Frocity":
            self.type = ["Ghost", "Ice"]
            self.moveset = ["Hollow Purple", "Infinite Void", "Star Finger", "RCT"]
        elif self.species == "Georift":
            self.type = ["Rock", "Steel"]
            self.moveset = ["Harden", "Steel Bash", "Roar", "Rock Throw"]
        else:
            self.type = ["Nothing"]
            self.moveset = ["Nothing"] * 4

        for i in range(len(self.type)):
            if self.type[i] == "Normal":
                self.attack += 0
                self.defense += 0
                self.speed += 0
                self.health += 0

            elif self.type[i] == "Fire":
                self.attack += 3
                self.defense += 3
                self.speed -= 2
                self.health -= 1

            elif self.type[i] == "Water":
                self.attack -= 1
                self.defense += 4
                self.speed += 3
                self.health -= 2

            elif self.type[i] == "Electric":
                self.attack -= 4
                self.defense -= 2
                self.speed += 4
                self.health += 1

            elif self.type[i] == "Grass":
                self.attack -= 4
                self.defense -= 3
                self.speed -= 1
                self.health += 7

            elif self.type[i] == "Ice":
                self.attack += 5
                self.defense -= 1
                self.speed += 2
                self.health += 2

            elif self.type[i] == "Fighting":
                self.attack += 4
                self.defense += 4
                self.speed += 2
                self.health -= 2

            elif self.type[i] == "Poison":
                self.attack += 2
                self.defense -= 2
                self.speed -= 1
                self.health += 0

            elif self.type[i] == "Ground":
                self.attack -= 2
                self.defense += 2
                self.speed += 4
                self.health += 3

            elif self.type[i] == "Flying":
                self.attack -= 2
                self.defense += 2
                self.speed += 4
                self.health -= 1

            elif self.type[i] == "Psychic":
                self.attack += 5
                self.defense -= 2
                self.speed += 1
                self.health += 3

            elif self.type[i] == "Bug":
                self.attack += 1
                self.defense += 3
                self.speed += 3
                self.health -= 2

            elif self.type[i] == "Rock":
                self.attack += 2
                self.defense += 5
                self.speed -= 4
                self.health += 1

            elif self.type[i] == "Ghost":
                self.attack += 2
                self.defense += 0
                self.speed += 3
                self.health -= 1

            elif self.type[i] == "Dragon":
                self.attack += 5
                self.defense += 4
                self.speed -= 1
                self.health -= 2

            elif self.type[i] == "Dark":
                self.attack += 2
                self.defense += 3
                self.speed -= 1
                self.health += 3

            elif self.type[i] == "Steel":
                self.attack -= 1
                self.defense += 4
                self.speed -= 2
                self.health -= 1

            elif self.type[i] == "Fairy":
                self.attack += 2
                self.defense -= 1
                self.speed += 3
                self.health -= 2

        self.currentHealth = self.health

    def set_species(self, species):
        self.species = species

    def get_currentHealth(self):
        return self.currentHealth

    def decrease_currentHealth(self):
        self.currentHealth = int(self.currentHealth*0.95)

    def increase_currentHealth(self):
        if self.currentHealth == self.health:
            pass
        else:
            self.currentHealth = self.currentHealth + ((self.health - self.currentHealth)*0.55)

    def get_moveset(self):
        return self.moveset
    def get_health(self):
        return self.health

    def get_type(self):
        return self.type
    def get_species(self):
        return self.species

    def get_attack(self):
        return self.attack

    def get_defense(self):
        return self.defense

    def get_speed(self):
        return self.speed

    def increaseAttack(self):
        self.attack = int(self.attack*1.1)

    def increaseDefense(self):
        self.defense = int(self.defense*1.05)

    def decreaseAttack(self):
        self.attack = int(self.attack*0.95)

    def decreaseDefense(self):
        self.defense = int(self.defense*0.97)

    def set_speed(self, multiplier):
        self.speed = self.speed*multiplier

    def takenDamage(self, damage):
        self.currentHealth -= damage
    def evolve(self):
        self.attack *= 2
        self.defense *= 4
        self.speed *= 3

    def is_alive(self):
        if self.currentHealth <= 0: return False
        else: return True
