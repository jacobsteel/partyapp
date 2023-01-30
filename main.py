#!/usr/bin/python
import mariadb
import sys

conn = mariadb.connect(
    user="root",
    password="",
    host="localhost",
    database="workplace")
cur = conn.cursor()


def add_data(first_name, last_name):
    try:
        statement = "INSERT INTO employees (first_name,last_name) VALUES (%s, %s)"
        data = (first_name, last_name)
        from mariadb._mariadb import cursor
        cursor.execute(statement, data)
        connection.commit()
        print("Successfully added entry to database")
    except database.Error as e:
        print(f"Error adding entry to database: {e}")

# retrieving information
#some_name = "Georgi"
#cur.execute("SELECT first_name,last_name FROM employees WHERE first_name=?", (some_name,))

#for first_name, last_name in cur:
#    print(f"First name: {first_name}, Last name: {last_name}")

# insert information

"""
try:
    cur.execute("INSERT INTO employees (first_name,last_name) VALUES (?, ?)", ("Maria", "DB"))
except mariadb.Error as e:
    print(f"Error: {e}")

conn.commit()
print(f"Last Inserted ID: {cur.lastrowid}")

conn.close()
"""




"""

# Module Imports
import mariadb
import sys

# Connect to MariaDB Platform
from mariadb._mariadb import cursor

try:
    conn = mariadb.connect(
        user="root",
        password="",
        host="127.0.0.1",
        port=3306,
        database="testowanie"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()


cursor.execute(
    "INSERT INTO guests (id, name, pref_food, isVegan) VALUES (?, ?, ?, ?)",
    (id, name, pref_food, isVegan)
)




"""
"""
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



"""
