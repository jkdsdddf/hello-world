import time

def introduction():
    print("Welcome to the Adventure Game!")
    time.sleep(1)
    print("You are standing at the entrance of a mysterious cave.")
    time.sleep(1)
    print("Your objective is to explore the cave and find the hidden treasure.")
    time.sleep(1)

def choose_path():
    choice = input("Which path will you choose? (left/right): ")
    if choice.lower() == "left":
        print("You take the left path and encounter a ferocious dragon!")
        time.sleep(1)
        print("What will you do?")
        time.sleep(1)
        # Rest of the scenario and choices
    elif choice.lower() == "right":
        print("You take the right path and find a locked door.")
        time.sleep(1)
        print("What will you do?")
        time.sleep(1)
        # Rest of the scenario and choices
    else:
        print("Invalid choice. Please choose again.")
        choose_path()

def main():
    introduction()
    choose_path()
    # Rest of the game logic

if __name__ == "__main__":
    main()