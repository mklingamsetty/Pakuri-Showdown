class PakuriMoves:
    def __init__(self):
        #moveDatabase = [["Move Name", "Damage Type", Does it do damage?,
        # Does it increase or decrease stats?, Does it apply debuff?, Does it hurt user?], ...]
        self.moveNameIndex = 0
        self.moveDamageTypeIndex = 1
        self.doesDamageIndex = 2
        self.buffIndex = 3
        self.deBuffIndex = 4
        self.selfHarmIndex = 5

        self.moveDatabase = [
            ["Absorb", "Grass", True, True, False, False],
            ["Agility", "Psychic", False, True, False, False],
            ["Ascend", "Flying", True, False, False, False],
            ["Aqua Jet", "Water", True, False, False, False],
            ["Astonish", "Ghost", True, False, False, False],
            ["Astral Barrage", "Ghost", True, False, False, False],
            ["Blitz", "Electric", True, False, False, False],
            ["Block", "Normal", False, True, False, False],
            ["Bite", "Normal", True, False, False, False],
            ["Bubble Beam", "Water", True, False, False, False],
            ["Bug Bite", "Bug", True, False, False, False],
            ["Buzz", "Electric", True, False, False, False],
            ["Charge", "Electric", False, True, False, False],
            ["Crunch", "Dark", True, False, False, False],
            ["Cleave", "Ghost", True, False, False, False],
            ["Crush Claw", "Dark", True, False, False, False],
            ["Dig", "Ground", True, False, False, False],
            ["Draco Meteor", "Dragon", True, False, False, False],
            ["Drill Peck", "Flying", True, False, False, False],
            ["Electro Ball", "Electric", True, False, False, False],
            ["Electro Web", "Electric", False, True, False, False],
            ["Ember", "Fire", True, False, False, False],
            ["Emerald Splash", "Normal", True, False, False, False],
            ["Flamethrower", "Fire", True, False, False, False],
            ["Fire Kick", "Fire", True, False, False, False],
            ["Fortify", "Rock", False, True, False, False],
            ["Frighten", "Ghost", True, False, False, False],
            ["Growl", "Normal", False, True, False, False],
            ["Growth", "Normal", True, False, False, False],
            ["Gust", "Flying", True, False, False, False],
            ["Haunt", "Ghost", True, False, False, False],
            ["Hollow Purple", "Ghost", True, False, False, False],
            ["Hydropump", "Water", True, False, False, False],
            ["Icy Shard", "Ice", True, False, False, False],
            ["Icy Wind", "Ice", True, False, False, False],
            ["Infinite Void", "Ice", False, True, False, False],
            ["Light of Ruin", "Fairy", True, False, False, True],
            ["Lightning Bolt", "Electric", True, False, False, False],
            ["Life Dew", "Water", False, True, False, False],
            ["Mega Punch", "Fighting", True, False, False, False],
            ["Mist", "Ice", True, False, False, False],
            ["Misty Explosion", "Fairy", True, False, False, False],
            ["Moonlight", "Fairy", False, True, False, False],
            ["Moongeist Beam", "Ghost", True, False, False, False],
            ["Mud Bomb", "Ground", True, False, False, False],
            ["Pump Up", "Fighting", False, True, False, False],
            ["Psywave", "Psychic", True, False, False, False],
            ["Rage Fist", "Ghost", True, False, False, False],
            ["Reflect", "Psychic", False, True, False, False],
            ["Roar", "Normal", False, True, False, False],
            ["Rock Blast", "Rock", True, False, False, False],
            ["Rock Throw", "Rock", True, False, False, False],
            ["Razor Shell", "Water", True, False, False, False],
            ["RCT", "Normal", True, False, False, False],
            ["Sacred Fire", "Fire", True, False, False, True],
            ["Scratch", "Normal", True, False, False, False],
            ["Seed Bomb", "Grass", True, False, False, False],
            ["Soul Buff", "Psychic", False, True, True, False],
            ["Star Finger", "Psychic", True, False, False, False],
            ["Steel Bash", "Steel", True, False, False, False],
            ["Sword Dance", "Normal", False, True, False, False],
            ["Toxic", "Poison", False, True, True, False],
            ["Vine Whip", "Grass", True, False, False, False],
            ["Wild Charge", "Electric", True, False, False, False],
            ["Will-O-Wisp", "Fire", False, True, False, False],
            ["Zen Headbutt", "Psychic", True, False, False, False],
            ["Za Warudo", "Dark", False, True, False, False]
        ]

    def get_moveDetails(self, name):

        for i in range(len(self.moveDatabase)):
            if self.moveDatabase[i][self.moveNameIndex] == name:

                return (
                        self.moveDatabase[i][self.moveDamageTypeIndex],
                        self.moveDatabase[i][self.doesDamageIndex],
                        self.moveDatabase[i][self.buffIndex],
                        self.moveDatabase[i][self.deBuffIndex],
                        self.moveDatabase[i][self.selfHarmIndex]
                )
