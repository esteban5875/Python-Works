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
                attack(attack_name="Tackle", type="Normal", damage=40, level="Start"),
                attack(attack_name="Growl", type="Normal", damage="None, lowers attack damage", level="Start"),
                attack(attack_name="Leech Seed", type="Grass", damage="Inflicts damage over time", level=7),
                attack(attack_name="Vine Whip", type="Grass", damage=45, level=13),
                attack(attack_name="Poison Powder", type="Poison", damage="None, poisons the target", level=20),
                attack(attack_name="Sleep Powder", type="Grass", damage="None, puts the target to sleep", level=27),
                attack(attack_name="Take Down", type="Normal", damage=90, level=34),
                attack(attack_name="Razor Leaf", type="Grass", damage=55, level=41),
                attack(attack_name="Sweet Scent", type="Normal", damage="None, lowers opponent's evasion", level=48),
                attack(attack_name="Growth", type="Normal", damage="None, raises user's Attack and Special Attack stats", level=55)
]

        )


#Test

#bulbasaur_instance = Bulbasaur()

# Print information about Bulbasaur
#print(f"Name: {bulbasaur_instance.name}")
#print(f"Species: {bulbasaur_instance.species}")
#print(f"XP: {bulbasaur_instance.pokemon_xp}")
#print(f"HP: {bulbasaur_instance.HP}")
#print(f"Types: {bulbasaur_instance.types}")
#print(f"Defense: {bulbasaur_instance.defense}")
#print(f"Speed: {bulbasaur_instance.speed}")

# Print information about special attacks
#print("\nAttacks:")
#for attack in bulbasaur_instance.attacks:
#    print(f"Attack Name: {attack.attack_name}")
#    print(f"Type: {attack.type}")
#    print(f"Damage: {attack.attack_damage}")
