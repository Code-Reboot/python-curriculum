import time
import random

potion = {
    "health": {
        "min": 2,
        "max": 5
    },
    "cost": 1
}

fists = {
    "damage": {
        "min": 1,
        "max": 3
    }
}

club = {
    "damage": {
        "min": 2,
        "max": 4
    },
    "cost": 5
}

axe = {
    "damage": {
        "min": 3,
        "max": 5
    },
    "cost": 10
}

sword = {
    "damage": {
        "min": 5,
        "max": 10
    },
    "cost": 20
}

enemy = {
    "health": {
        "min": 4,
        "max": 12
    },
    "damage": {
        "min": 0,
        "max": 2
    },
    "gold": {
        "min": 2,
        "max": 5
    }
}

character = {
    "health": 20,
    "current_weapon": "fists",
    "unlocked": {
        "club": False,
        "axe": False,
        "sword": False
    },
    "potions": 1,
    "gold": 0
}


def shop():
    print("[Narrator] " + character["name"] + " entered the shop with " + str(character["gold"]) + " gold in their pocket!")
    if character["unlocked"]["club"] == False:
        print(" - exit")
        print(" - potion | " + str(potion["health"]["min"]) + " - " + str(potion["health"]["max"]) + " health | " + str(
            potion["cost"]) + " gold")
        print(" - club | " + str(club["damage"]["min"]) + " - " + str(club["damage"]["max"]) + " damage | " + str(
            club["cost"]) + " gold")
        print(" - axe | " + str(axe["damage"]["min"]) + " - " + str(axe["damage"]["max"]) + " damage | " + str(
            axe["cost"]) + " gold")
        print(" - sword | " + str(sword["damage"]["min"]) + " - " + str(sword["damage"]["max"]) + " damage | " + str(
            sword["cost"]) + " gold")

        choice = input(">>> ")
        if choice == "exit":
            print("[Narrator] " + character["name"] + " left the shop.")
            time.sleep(2)
            menu()
        elif choice == "potion":
            if character["gold"] >= potion["cost"]:
                character["gold"] -= potion["cost"]
                character["potions"] += 1
                print("[Narrator] " + character["name"] + " just bought a potion!")
                time.sleep(2)
                shop()
            else:
                print("[Narrator] " + character["name"] + " doesn't have enough money!")
                time.sleep(2)
                shop()
        elif choice == "club":
            if character["gold"] >= club["cost"]:
                character["gold"] -= club["cost"]
                character["current_weapon"] = "club"
                character["unlocked"]["club"] = True
                print("[Narrator] " + character["name"] + " just bought a club!")
                time.sleep(2)
                shop()
            else:
                print("[Narrator] " + character["name"] + " doesn't have enough money!")
                time.sleep(2)
                shop()
        elif choice == "axe":
            if character["gold"] >= axe["cost"]:
                character["gold"] -= axe["cost"]
                character["current_weapon"] = "axe"
                character["unlocked"]["axe"] = True
                print("[Narrator] " + character["name"] + " just bought an axe!")
                time.sleep(2)
                shop()
            else:
                print("[Narrator] " + character["name"] + " doesn't have enough money!")
                time.sleep(2)
                shop()
        elif choice == "sword":
            if character["gold"] >= sword["cost"]:
                character["gold"] -= sword["cost"]
                character["current_weapon"] = "sword"
                character["unlocked"]["sword"] = True
                print("[Narrator] " + character["name"] + " just bought a sword!")
                time.sleep(2)
                shop()
            else:
                print("[Narrator] " + character["name"] + " doesn't have enough money!")
                time.sleep(2)
                shop()
        else:
            print("[Narrator] That option wasn't recognized. Please try again.")
            time.sleep(2)
            shop()


def potion_drink():
    if character["potions"] > 0:
        health = random.randint(potion["health"]["min"], potion["health"]["max"])
        character["health"] += health
        print("[Narrator] " + character["name"] + " gained " + str(health) + " health by drinking a potion!")
        character["potions"] -= 1
        print("[Narrator] " + character["name"] + " has " + str(character["potions"]) + " potions left.")
        time.sleep(2)
        menu()
    else:
        print("[Narrator] " + character["name"] + " doesn't have any potions to drink!")
        time.sleep(2)
        menu()


def enemy_attack(new_enemy):
    character["health"] -= new_enemy["damage"]
    print("[Enemy] Attacked " + character["name"] + " with " + str(new_enemy["damage"]) + " damage")
    if character["health"] < 0:
        print("[Narrator] " + character["name"] + " is now at 0 health.")
    else:
        print("[Narrator] " + character["name"] + " is now at " + str(character["health"]) + " health.")
    time.sleep(1)


def player_attack(new_enemy):
    if character["current_weapon"] == "fists":
        turn_damage = random.randint(fists["damage"]["min"], fists["damage"]["max"])
    elif character["current_weapon"] == "club":
        turn_damage = random.randint(club["damage"]["min"], club["damage"]["max"])
    elif character["current_weapon"] == "axe":
        turn_damage = random.randint(axe["damage"]["min"], axe["damage"]["max"])
    else:
        turn_damage = random.randint(sword["damage"]["min"], sword["damage"]["max"])
    new_enemy["health"] -= turn_damage
    print("[" + character["name"] + "] Attacked Enemy with " + str(turn_damage) + " damage")
    if new_enemy["health"] < 0:
        print("[Enemy] Is now at 0 health.")
    else:
        print("[Enemy] Is now at " + str(new_enemy["health"]) + " health.")
    time.sleep(1)


def arena():
    attack_last = ""
    print("[Narrator] " + character["name"] + " entered the arena ready to face a worth opponent!")
    new_enemy = {
        "health": random.randint(enemy["health"]["min"], enemy["health"]["max"]),
        "damage": random.randint(enemy["damage"]["min"], enemy["damage"]["max"]),
        "gold": random.randint(enemy["gold"]["min"], enemy["gold"]["max"]),
    }
    first_move = random.randint(0, 1)
    if first_move == 0:
        print("[Narrator] " + character["name"] + " will make the first move!")
        time.sleep(2)
        player_attack(new_enemy)
        attack_last = "player"
    else:
        print("[Narrator] Out of nowhere, an enemy attacked!")
        enemy_attack(new_enemy)
        attack_last = "enemy"
    while character["health"] > 0 and new_enemy["health"] > 0:
        if attack_last == "player":
            enemy_attack(new_enemy)
            attack_last = "enemy"
        elif attack_last == "enemy":
            player_attack(new_enemy)
            attack_last = "player"
    if character["health"] < 1:
        print("[Narrator] After a long and hard battle, " + character["name"] + " lost and died.")
        character["health"] = 0
        print("[Narrator] " + character["name"] + " finished with " + str(character["health"]) + " health, their " +
              character[
                  "current_weapon"] + ", " + str(character["potions"]) + " potions, and " + str(
            character["gold"]) + " gold.")
    else:
        print("[Narrator] " + character["name"] + " won and was awarded " + str(new_enemy["gold"]) + " gold!")
        character["gold"] += new_enemy["gold"]
        time.sleep(2)
        menu()


def menu():
    print(
        "[Narrator] " + character["name"] + " has " + str(character["health"]) + " health, is using their " + character[
            "current_weapon"] + " to fight, and has " + str(character["gold"]) + " gold.")
    print("[Narrator] You may go to the shop, the arena, or use a potion.")
    print(" - exit")
    print(" - shop")
    print(" - arena")
    print(" - potion")

    choice = input(">>> ")
    if choice == "exit":
        print("[Narrator] " + character["name"] + " finished with " + str(character["health"]) + " health, their " +
              character[
                  "current_weapon"] + ", " + str(character["potions"]) + " potions, and " + str(
            character["gold"]) + " gold.")
    elif choice == "shop":
        shop()
    elif choice == "arena":
        arena()
    elif choice == "potion":
        potion_drink()
    else:
        print("[Narrator] That option wasn't recognized. Please try again.")
        time.sleep(2)
        menu()


character["name"] = input("[Narrator] What is your character's name?\n>>> ")
menu()
