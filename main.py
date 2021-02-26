while True:  # Runs game until player does not type yes
    answer = input("Would you like to play this game? [Yes/No] ")

    if answer.lower().strip() == "Yes":

        answer = input("You reach a crossroads, would you like to go Left or Right?").lower().strip()
        if answer == "Left":
            answer = input("You encounter a monster. Do you want to run or attack?")

            if answer == "attack":
                print("You have no weapons - That was stupid. -- You died.")
            else:
                print("Excellent choice. You made it away safely.")

                answer = input("You see a car and a plane. Which will you take? (Car/Plane)")
                if answer == "Plane":
                    print("You do not know how to fly a plane. You crash and die.")
                else:
                    print("It's a Tesla. You won!")

        elif answer == "right":
            print("You take one step and fall into quicksand. Sorry, but you die here.")

        else:
            print("Invalid choice, you lost!")

    else:
        print("That's too bad.")
    answer = input("Would you like to play this game? [Yes/No] ")

    if answer.lower().strip() == "Yes":

        answer = input("You reach a crossroads, would you like to go Left or Right?").lower().strip()
        if answer == "Left":
            answer = input("You encounter a monster. Do you want to run or attack?")

            if answer == "attack":
                print("You have no weapons - That was stupid. -- You died.")
            else:
                print("Excellent choice. You made it away safely.")

                answer = input("You see a car and a plane. Which will you take? (Car/Plane)")
                if answer == "Plane":
                    print("You do not know how to fly a plane. You crash and die.")
                else:
                    print("It's a Tesla. You won!")

        elif answer == "right":
            print("You take one step and fall into quicksand. Sorry, but you die here.")

        else:
            print("Invalid choice, you lost!")

    else:
        print("That's too bad.")
        break
