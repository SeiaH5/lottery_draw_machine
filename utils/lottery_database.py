import sqlite3

connection = sqlite3.connect("lottery_data.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS tickets(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    gamemode INTEGER,
    numbers TEXT,
    draw_numbers TEXT,
    matches INTEGER
)
""")

connection.commit()

def register_user(username, password):
    try:
        cursor.execute("INSERT INTO users(username,password) VALUES(?,?)",(username,password))
        connection.commit()
        return True
    except:
        return False

def login_user(username, password):
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?",(username,password))
    return cursor.fetchone()

def save_ticket(username, gamemode, numbers, draw_numbers, matches):
    cursor.execute(
        "INSERT INTO tickets(username,gamemode,numbers,draw_numbers,matches) VALUES(?,?,?,?,?)",
        (username, gamemode, str(numbers), str(draw_numbers), matches)
    )
    connection.commit()

def get_user_tickets(username):
    cursor.execute("SELECT gamemode,numbers,draw_numbers,matches FROM tickets WHERE username=?",(username,))
    return cursor.fetchall()