print("==============================")
print("       MINI BATTLE GAME")
print("==============================")

# Player setup
name = input("Enter your player name: ")

player = {
    "name": name,
    "health": 100,
    "attack": 20,
    "defense": 10,
    "potions": 3,
    "coins": 0
}

# Enemies
enemies = [
    {
        "name": "Goblin",
        "health": 50,
        "attack": 10,
        "reward": 20
    },
    {
        "name": "Wolf",
        "health": 70,
        "attack": 15,
        "reward": 30
    },
    {
        "name": "Skeleton",
        "health": 90,
        "attack": 18,
        "reward": 50
    },
    {
        "name": "Dragon",
        "health": 120,
        "attack": 25,
        "reward": 100
    }
]

# Defeated enemies
defeated_enemies = set()


# View player
def view_player():
    print("\n==============================")
    print("        PLAYER STATUS")
    print("==============================")

    print(f"Name: {player['name']}")
    print(f"Health: {player['health']}")
    print(f"Attack: {player['attack']}")
    print(f"Defense: {player['defense']}")
    print(f"Potions: {player['potions']}")
    print(f"Coins: {player['coins']}")


# View enemies
def view_enemies():
    print("\n==============================")
    print("        AVAILABLE ENEMIES")
    print("==============================")

    for enemy in enemies:
        if enemy["name"] in defeated_enemies:
            status = "DEFEATED"
        else:
            status = "AVAILABLE"

        print("------------------------------")
        print(f"Name: {enemy['name']}")
        print(f"Health: {enemy['health']}")
        print(f"Attack: {enemy['attack']}")
        print(f"Reward: {enemy['reward']}")
        print(f"Status: {status}")


# Use potion
def use_potion():
    if player["potions"] > 0:

        if player["health"] < 100:
            player["health"] += 30

            if player["health"] > 100:
                player["health"] = 100

            player["potions"] -= 1

            print("\nYou used a potion!")
            print(f"Health: {player['health']}")
            print(f"Potions left: {player['potions']}")

        else:
            print("\nYour health is already full!")

    else:
        print("\nYou don't have any potions!")


# Fight enemy
def fight_enemy():

    print("\n==============================")
    print("          CHOOSE ENEMY")
    print("==============================")

    for i in range(len(enemies)):
        enemy = enemies[i]

        if enemy["name"] not in defeated_enemies:
            print(f"{i + 1}. {enemy['name']}")

    choice = input("Choose enemy number: ")

    if choice.isdigit():

        choice = int(choice)

        if choice >= 1 and choice <= len(enemies):

            enemy = enemies[choice - 1]

            if enemy["name"] in defeated_enemies:
                print("\nYou already defeated this enemy!")
                return

            enemy_health = enemy["health"]

            print(f"\nYou are fighting {enemy['name']}!")

            while enemy_health > 0 and player["health"] > 0:

                print("\n------------------------------")
                print(f"Your Health: {player['health']}")
                print(f"{enemy['name']} Health: {enemy_health}")
                print("------------------------------")

                print("1. Attack")
                print("2. Use Potion")
                print("3. Run")

                action = input("Choose action: ")

                if action == "1":

                    damage = player["attack"] - (enemy["attack"] // 4)

                    if damage < 1:
                        damage = 1

                    enemy_health -= damage

                    print(f"\nYou attacked {enemy['name']}!")
                    print(f"You dealt {damage} damage.")

                    if enemy_health <= 0:
                        print(f"\n🎉 You defeated {enemy['name']}!")

                        player["coins"] += enemy["reward"]
                        defeated_enemies.add(enemy["name"])

                        print(f"You earned {enemy['reward']} coins.")
                        print(f"Total coins: {player['coins']}")

                        break

                    # Enemy attacks
                    enemy_damage = enemy["attack"] - player["defense"]

                    if enemy_damage < 1:
                        enemy_damage = 1

                    player["health"] -= enemy_damage

                    print(f"{enemy['name']} attacked you!")
                    print(f"You lost {enemy_damage} health.")

                elif action == "2":

                    use_potion()

                elif action == "3":

                    print("\nYou ran away from the battle!")
                    break

                else:

                    print("\nInvalid choice!")

            if player["health"] <= 0:
                print("\n You have been defeated!")
                print("Game Over!")

        else:
            print("\nInvalid enemy number!")

    else:
        print("\nPlease enter a valid number.")


# Main game loop
while True:

    print("\n==============================")
    print("          MAIN MENU")
    print("==============================")

    print("1. View Player")
    print("2. View Enemies")
    print("3. Fight Enemy")
    print("4. Use Potion")
    print("5. View Defeated Enemies")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        view_player()

    elif choice == "2":

        view_enemies()

    elif choice == "3":

        if player["health"] > 0:
            fight_enemy()
        else:
            print("\nYou cannot fight. Game Over!")

    elif choice == "4":

        use_potion()

    elif choice == "5":

        print("\n==============================")
        print("       DEFEATED ENEMIES")
        print("==============================")

        if len(defeated_enemies) == 0:
            print("No enemies defeated yet.")
        else:
            for enemy in defeated_enemies:
                print("-", enemy)

    elif choice == "6":

        print("\nThanks for playing!")
        print(f"Final Coins: {player['coins']}")
        print(f"Enemies Defeated: {len(defeated_enemies)}")
        break

    else:

        print("\nInvalid choice! Please try again.")