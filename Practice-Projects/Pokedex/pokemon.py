

class pokemon():
    def __init__(self, pokemon_xp, attacks, species, name, types, HP, defense, speed):
        self.name = name
        self.species = species
        self.pokemon_xp = pokemon_xp
        self.types = types
        self.HP = HP
        self.defense = defense
        self.speed = speed
        self.attacks = attacks

class attack():
    def __init__(self, attack_name, attack_damage, level_required, type):
        self.attack_name = attack_name
        self.attack_damage = attack_damage
        self.level_required = level_required
        self.type = type
