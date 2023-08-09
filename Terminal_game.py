import random
import time

# RPG Terminal Game

# Type of character
    # Samurai 🗡️ 
    # Ninja 🥷
    # Wizard 🧙‍♂️
    # Alien 👽

time.sleep(0.5)

print("================================================================\n                    Welcome to my game.\n                      By Jorge Flores\n================================================================")

time.sleep(1)

character = int(input("\n1)🗡️  Samurai\n2)🥷  Ninja\n3)🧙‍♂️ Wizard\n4)👽 Alien\n\nSelect your character. "))

time.sleep(2)

if character == 1:
    type_character = "Samurai"
    powers = ["Stomp","Slash"]
    villan_name = "Genji"
    print("\nYou selected: 🗡️  Samurai")
elif character == 2:
    type_character = "Ninja"
    powers = ["Kunai","Poison"]
    villan_name = "Shredder"
    print("\nYou selected:🥷  Ninja")
elif character == 3:
    type_character = "Wizard"
    powers = ["Fire Ball","Enchantment"]
    villan_name = "Ged"
    print("\nYou selected:🧙‍♂️  Wizard")
elif character == 4:
    type_character = "Alien"
    powers = ["Telekinesis","Heat Vision"]
    villan_name = "Xeno"
    print("\nYou selected:👽  Alien")
else:
    print("Something is wrong...")

time.sleep(1)

character_name = input("\nEnter name: ")
cap_char_name = character_name.capitalize()

time.sleep(1.5)
print("\n✨ A GREAT LEGEND WOKE UP✨")
time.sleep(2.1)
print("\nThe is Year 3020.")
time.sleep(1.7)
print(f"\nThe {type_character} {cap_char_name} has been frozen for 200 years. ")
time.sleep(1.8)
print(f"\nThe world is being ruled by the great villan {villan_name}.\n")
time.sleep(2)
print("...\n")
time.sleep(3)


print(f"{cap_char_name} woke up realzing that the world is crumbling.\n")
time.sleep(2)
print(f"{cap_char_name}: I must do something about this!\n")

# Ask player what they want to do.

time.sleep(2)
user_choice = int(input(f"1) Go defeat {villan_name} 👊\n2) Go home🏠\n3) Go back being frozen🥶\n\nChoose: "))

if user_choice == 1:
    print("\n*Teleporting to final Boss*\n")

    time.sleep(2)
    print(f"{villan_name}: Ahhhh, I was waiting for you!\n")
    time.sleep(1.5)
    print(f"{cap_char_name} : NO TALKING! Let's go!\n")
    time.sleep(1)

    hero_health = 100
    vil_health = 100
    

    while hero_health > 0 and vil_health > 0:

        user_attack = int(input(f"Powers:\n1) {powers[0]} (15 dmg)\n2) {powers[1]} (35 dmg)\n\nSelect Power: "))

        if user_attack == 1:
            vil_health -= 15
        elif user_attack == 2:
            vil_health -= 35
        else:
            print("Something is wrong...")

        time.sleep(1)

        hero_health -= 20

        print(f"\n{villan_name} is attacking. 20 dmg")

        time.sleep(1.5)

        
        print(f"\n{villan_name} Health: {vil_health}")
        print(f"{cap_char_name} Health: {hero_health}\n")
        time.sleep(1)


        if hero_health <= 0:
            print("You failed.\n")
            print("The gods aske themselves why")
            print("The END")
        elif vil_health <= 0:
            print("YOU WON!\n")
            print("The wolrd was saved and everyone got a free Taco.\nSomeone screamed: please no Tacos from Tacobell.")
            print("The END!.")

elif user_choice == 2:
    print("\n*Teleporting home*\n")

    time.sleep(2)
    print("Nothing was there. Everything was destroyed...\n")

    time.sleep(1.5)
    print(f"with rage the {type_character} {cap_char_name} screamed.\n")
    time.sleep(1)
    print(f"{cap_char_name}: What should I do now?\n")
    time.sleep(1)
    user_choice_two = int(input(f"1) Do nothing\n2) Find something to eat\n3) Defeat {villan_name}\n\nChoose: "))  

    if user_choice_two == 1:
        print(f"{cap_char_name} does nothing.\n")
        print("The world was destoyed.")
        print("The END.")
    elif user_choice_two == 2:
        print(f"\n{cap_char_name} found some 🌮 tacos!\n")
        time.sleep(1)
        print(f"{cap_char_name} ate and ate until the belly was full.")
        print(f"The END!")

    elif user_choice_two == 3:
        print("*Teleporting to final Boss*\n")
        time.sleep(2)
        print(f"{villan_name}: Ahhhh, I was waiting for you!\n")
        time.sleep(1.5)
        print(f"{cap_char_name} : NO TALKING! Let's go!\n")
        time.sleep(1)

        hero_health = 100
        vil_health = 100
        
        while hero_health > 0 and vil_health > 0:
            user_attack = int(input(f"Powers:\n1) {powers[0]} (15 dmg)\n2) {powers[1]} (35 dmg)\n\nSelect Power: "))

            if user_attack == 1:
                vil_health -= 15
            elif user_attack == 2:
                vil_health -= 35
            else:
                print("Something is wrong...")

            time.sleep(1)

            hero_health -= 20

            print(f"\n{villan_name} is attacking. 20 dmg")

            time.sleep(1.5)

            print(f"\n{villan_name} Health: {vil_health}")
            print(f"{cap_char_name} Health: {hero_health}\n")
            time.sleep(1)

            if hero_health <= 0:
                print("You failed.")
                print("The gods aske themselves why")
                print("The END")
            elif vil_health <= 0:
                print("YOU WON!")
                print("The wolrd was saved and everyone got a free Taco.\nSomeone screamed: please no Tacos from Tacobell.")
                print("The END!.")

        else:
            print("Something is wrong...")

elif user_choice == 3:
    print("\nScrew this...\n")
    print(f"{cap_char_name} never cared and the gods are pissed.")
    print(f"The gods came down and vanished {cap_char_name}")
    print("THE END.\n")
else:
    print("Something is wrong...")