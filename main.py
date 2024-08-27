import random
from character import Character

def main():
    print("Welcome to New Fantasy!")
    player_name = input("Please enter your nickname: \n")
    print("Please select your class: \n")
    print("1. Paladin")
    print("2. Druid")
    print("3. Mage")
    print("4. Necromancer")
    job_option = int(input("Your class? (1-4): \n"))

    job = {1: "Paladin", 2: "Druid", 3: "Mage", 4: "Necromancer"}
    player_job = job.get(job_option, "Paladin")  # Paladin por defecto si elige una opción inválida

    player = Character(player_name, player_job)
    orc = Character("Orco", pclass="Mob", level=1, exp=50)
    wolf = Character("Lobo", pclass="Mob", level=2, exp=60)
    dragon = Character("Dragón", pclass="Mob", level=3, exp=100)

    print("\nYour Character Summary")
    print(player.status)

    mobs = {
        'Orco': {'object': orc, 'exp_gain': 50, 'exp_loss': 30},
        'Lobo': {'object': wolf, 'exp_gain': 75, 'exp_loss': 65},
        'Dragón': {'object': dragon, 'exp_gain': 100, 'exp_loss': 110},
    }

    while True:
        mobname, mob_info = random.choice(list(mobs.items()))
        mob = mob_info['object']
        exp_gain = mob_info['exp_gain']
        exp_loss = mob_info['exp_loss']

        probability = player.winprobability(mob)

        print(f"\nYou have encountered a {mobname}")
        option = Character.fightmode(mobname, probability, exp_gain, exp_loss)

        if option != 1:
            print("\nYou tried to escape..... the escape was successful")
            break

        result = random.uniform(0, 1)

        if result <= probability:
            print(f"\nYou won against {mobname}!")
            print(f"\nEXP gained: {exp_gain} points")
            player.status = exp_gain
            mob.status = -exp_loss
        else:
            print(f"\nYou were defeated by {mobname}!")
            print(f"\nEXP lost: {exp_loss} points")
            player.status = -exp_loss
            mob.status = exp_gain

        print("\nYour status:")
        print(player.status)

        print("\nMob Status:")
        print(mob.status)

if __name__ == "__main__":
    main()
