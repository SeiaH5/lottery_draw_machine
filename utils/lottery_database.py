import json
import os

database_file = "lottery_data.json"

def load_database():
    if not os.path.exists(database_file):
        data = {"users": {}, "tickets": []}
        save_database(data)
    with open(database_file, "r") as file:
        return json.load(file)

def save_database(data):
    with open(database_file, "w") as file:
        json.dump(data, file, indent=4)

def register_user(username, password):
    data = load_database()
    if username in data["users"]:
        return False
    data["users"][username] = password
    save_database(data)
    return True

def login_user(username, password):
    data = load_database()
    if username in data["users"] and data["users"][username] == password:
        return True
    return False

def save_ticket(username, gamemode, numbers, draw_numbers, matches):
    data = load_database()
    ticket = {
        "username": username,
        "gamemode": "6/"+f"{gamemode}",
        "numbers": numbers,
        "draw_numbers": draw_numbers,
        "matches": matches
    }
    data["tickets"].append(ticket)
    save_database(data)

def get_user_tickets(username):
    data = load_database()
    return [ticket for ticket in data["tickets"] if ticket["username"] == username]