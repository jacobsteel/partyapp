start_options = ["1. Food", "2. Guests", "3. Transportation", "4. Quittest"]

food = ["Cake", "Donut", "Tofu", "Chicken"]
guests = ["Derek", "Christopher", "Daryl"]
transportation = "Are you going to drive home by car? (Y/N)"


is_Vegan = "Are you Vegan? (Y/N)" #food availability

def start():
    print(start_options)
    option = input()

    if option == "1":
        print(food)
        go_back()
    elif option == "2":
        guest()
    elif option == "3":
        print(transportation)
        ask_transportation()
        go_back()
    elif option == "4":
        go_away()
    else:
        print("Invalid Information")
        go_back()


def go_back():
    ask = input("Do you want to go back? (Y/N)")
    if ask == "Y":
        start()
    elif ask == "N":
        print("See you later!")
        quit()
    else:
        print("Invalid Information")
        go_back()


def ask_transportation():
    transport_answer = input()
    if transport_answer == "Y":
        print("You are not allowed to drink alcohol")
    elif transport_answer == "N":
        print("You are allowed to drink alcohol")
    else:
        print("Insert valid value!")

def go_away():
    answer = input("Do you want to leave? (Y/N)")
    if answer == "Y":
        quit()
    elif answer == "N":
        start()
    else:
        print("Invalid option!")


def guest():
    print(guests)
    adding = input("Do you want to add yourself to the list? Y/N")
    if adding == "Y":
        guests.append(name)
        print(guests)
        go_back()
    elif adding == "N":
        removing = input("Do you want to remove yourself from the list? Y/N")
        if removing == "Y":
            guests.remove(name)
            print(guests)
            go_back()
        elif removing == "N":
            go_back()
        else:
            print("Invalid option!")
            go_back()
    else:
        print("Invalid option!")
        go_back()
    print(guests)



print("Welcome to party app. Please insert your name: ")
name = input()
print("Hello " + name + ". Please choose your option")
start()
