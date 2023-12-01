from pokemon import *

class Bulbasaur(pokemon):
    
    def __init__(self):
        super().__init__(
            name = "Bulbasaur",
            species = "Seed Pokemon",
            pokemon_xp = 64,
            HP = 45,
            types = ["Grass"],
            defense = 49,
            speed = 45,
            attacks = [
                attack(attack_name="Growl", type="Normal", attack_damage="None, lowers attack damage", level_required="Start"),
                attack(attack_name="Tackle", type="Normal", attack_damage=40, level_required="Start"),
                attack(attack_name="Leech Seed", type="Grass", attack_damage="Inflicts damage over time", level_required=7),
                attack(attack_name="Vine Whip", type="Grass", attack_damage=45, level_required=13),
                attack(attack_name="Poison Powder", type="Poison", attack_damage="None, poisons the target", level_required=20),
                attack(attack_name="Sleep Powder", type="Grass", attack_damage="None, puts the target to sleep", level_required=27),
                attack(attack_name="Take Down", type="Normal", attack_damage=90, level_required=34),
                attack(attack_name="Razor Leaf", type="Grass", attack_damage=55, level_required=41),
                attack(attack_name="Sweet Scent", type="Normal", attack_damage="None, lowers opponent's evasion", level_required=48),
                attack(attack_name="Growth", type="Normal", attack_damage="None, raises user's Attack and Special Attack stats", level_required=55)
]

        )

class Ivysaur(pokemon):
    Evolution_from = Bulbasaur()
    Inherited_attacks = Evolution_from.attacks
    parent = "Bulbasaur"

    Inherited_attacks.extend([
        attack(attack_name="Vine Whip", type="Grass", attack_damage=45, level_required=13),
        attack(attack_name="Poison Powder", type="Poison", attack_damage="Inflicts poison on the opponent, causing damage at the end of each turn.", level_required=15),
        attack(attack_name="Sleep Powder", type="Grass", attack_damage="Puts the opponent to sleep, rendering it unable to act for a number of turns.", level_required=18),
        attack(attack_name="Take Down", type="Normal", attack_damage=90, level_required=23)
    ])

    def __init__(self):
        super().__init__(
            name="Ivysaur",
            species="Seed Pokemon",
            pokemon_xp=142,
            HP=60,
            types=["Grass", "Poison"],
            defense=63,
            speed=60,
            attacks=Ivysaur.Inherited_attacks
        )

from pokemon import *

class Bulbasaur(pokemon):
    
    def __init__(self):
        super().__init__(
            name = "Bulbasaur",
            species = "Seed Pokemon",
            pokemon_xp = 64,
            HP = 45,
            types = ["Grass"],
            defense = 49,
            speed = 45,
            attacks = [
                attack(attack_name="Growl", type="Normal", attack_damage="None, lowers attack damage", level_required="Start"),
                attack(attack_name="Tackle", type="Normal", attack_damage=40, level_required="Start"),
                attack(attack_name="Leech Seed", type="Grass", attack_damage="Inflicts damage over time", level_required=7),
                attack(attack_name="Vine Whip", type="Grass", attack_damage=45, level_required=13),
                attack(attack_name="Poison Powder", type="Poison", attack_damage="None, poisons the target", level_required=20),
                attack(attack_name="Sleep Powder", type="Grass", attack_damage="None, puts the target to sleep", level_required=27),
                attack(attack_name="Take Down", type="Normal", attack_damage=90, level_required=34),
                attack(attack_name="Razor Leaf", type="Grass", attack_damage=55, level_required=41),
                attack(attack_name="Sweet Scent", type="Normal", attack_damage="None, lowers opponent's evasion", level_required=48),
                attack(attack_name="Growth", type="Normal", attack_damage="None, raises user's Attack and Special Attack stats", level_required=55)
]

        )

class Ivysaur(pokemon):
    Evolution_from = Bulbasaur()
    Inherited_attacks = Evolution_from.attacks
    parent = "Bulbasaur"

    Inherited_attacks.extend([
        attack(attack_name="Vine Whip", type="Grass", attack_damage=45, level_required=13),
        attack(attack_name="Poison Powder", type="Poison", attack_damage="Inflicts poison on the opponent, causing damage at the end of each turn.", level_required=15),
        attack(attack_name="Sleep Powder", type="Grass", attack_damage="Puts the opponent to sleep, rendering it unable to act for a number of turns.", level_required=18),
        attack(attack_name="Take Down", type="Normal", attack_damage=90, level_required=23)
    ])

    def __init__(self):
        super().__init__(
            name="Ivysaur",
            species="Seed Pokemon",
            pokemon_xp=142,
            HP=60,
            types=["Grass", "Poison"],
            defense=63,
            speed=60,
            attacks=Ivysaur.Inherited_attacks
        )

class Venusaur(pokemon):
    Evolution_from = Ivysaur()
    Inherited_attacks = Evolution_from.attacks
    parent = "Ivysaur"




#Tests

# Test Bulbasaur
#print("Testing Bulbasaur:")
#bulbasaur = Bulbasaur()
#print(f"Name: {bulbasaur.name}")
#print(f"Species: {bulbasaur.species}")
#print(f"XP: {bulbasaur.pokemon_xp}")
#print(f"HP: {bulbasaur.HP}")
#print(f"Types: {bulbasaur.types}")
#print(f"Defense: {bulbasaur.defense}")
#print(f"Speed: {bulbasaur.speed}")
#
#print("Attacks:")
#for i, attack in enumerate(bulbasaur.attacks):
#    print(f"{i+1}. Attack Name: {attack.attack_name}, Type: {attack.type}, Damage: {attack.attack_damage}, Level: {attack.level_required}")
#
## Test Ivysaur
#print("\nTesting Ivysaur:")
#ivysaur = Ivysaur()
#print(f"Name: {ivysaur.name}")
#print(f"Species: {ivysaur.species}")
#print(f"XP: {ivysaur.pokemon_xp}")
#print(f"HP: {ivysaur.HP}")
#print(f"Types: {ivysaur.types}")
#print(f"Defense: {ivysaur.defense}")
#print(f"Speed: {ivysaur.speed}")
#
#print("Attacks:")
#for i, attack in enumerate(ivysaur.attacks):
#    print(f"{i+1}. Attack Name: {attack.attack_name}, Type: {attack.type}, Damage: {attack.attack_damage}, Level: {attack.level_required}")
#
