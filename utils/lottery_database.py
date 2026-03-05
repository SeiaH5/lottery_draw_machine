import sqlite3

connection = sqlite3.connect("lottery_data.db")
cursor = connection.cursor()

def create_tables():
    cursor.execute("""
    create table if not exists users(
        id integer primary key autoincrement,
        username text unique,
        password text
    )
    """)
    cursor.execute("""
    create table if not exists tickets(
        id integer primary key autoincrement,
        username text,
        gamemode integer,
        numbers text,
        draw_numbers text,
        matches integer
    )
    """)
    connection.commit()

def register_user(username,password):
    try:
        cursor.execute("insert into users(username,password) values(?,?)",(username,password))
        connection.commit()
        return True
    except:
        return False

def login_user(username,password):
    cursor.execute("select * from users where username=? and password=?",(username,password))
    return cursor.fetchone()

def save_ticket(username,gamemode,numbers,draw_numbers,matches):
    cursor.execute(
        "insert into tickets(username,gamemode,numbers,draw_numbers,matches) values(?,?,?,?,?)",
        (username,gamemode,str(numbers),str(draw_numbers),matches)
    )
    connection.commit()

def get_user_tickets(username):
    cursor.execute("select gamemode,numbers,draw_numbers,matches from tickets where username=?",(username,))
    return cursor.fetchall()

create_tables()