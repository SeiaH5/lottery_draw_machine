from utils import lottery_login,lottery_database
import lottery_draw_machine

#Main menu
def menu():
    while True:
        print(f"""{"-"*30}\033[1m
        MENU \033[0m

    \033[1m[P]\033[0m Play
    \033[1m[T]\033[0m Tickets
    \033[1m[I]\033[0m Instruction
    \033[1m[L]\033[0m Log out
    
    \033[1m[0]\033[0m Exit
        """)
        menu_select = input("Select menu: ").upper()
        print("-"*30)
        print("\n"*5)
        if menu_select == "P":
            return lottery_draw_machine.main()
        elif menu_select == "T":
            return show_tickets()
        elif menu_select == "I":
            return instruction()
        elif menu_select == "L":
            print("\n\033[1mLogging out...\033[0m\n")
            lottery_login.front_panel()
        elif menu_select == "0":
            exit()
        else:
            print("\033[31mInvalid menu option.\033[0m")

#Shows user's ticket/s
def show_tickets():
    user = lottery_login.current_user
    tickets = lottery_database.get_user_tickets(user)
    if not tickets:
        print("No tickets found.")
    else:
        for t in tickets:
            print(f"{t['gamemode']} : {t['numbers']} -> drawn: {t['draw_numbers']} match: {t['matches']}")
    while True:
        tickets_option = input("\n[0] Go back to menu...")
        if tickets_option == "0":
            print("-"*30)
            menu()
        else:
            print("\033[31mInvalid input.\033[0m\n")
            continue

# Gamemode selector
def gamemode():
    while True:
        try:
            print("""Gamemodes:
[1] 6/42 -  Players draw six numbers from a pool of 42. 
            The jackpot is the largest among these games, 
            with a minimum guaranteed amount of ₱10,000.00 for the 1st Prize.
            The game is considered easier to win compared to others with larger pools.
[2] 6/45 -  Players draw six numbers from a pool of 45. 
            The jackpot amount varies based on ticket sales, 
            making it more challenging to win compared to the 6/42 game. 
[3] 6/49 -  Players draw six numbers from a pool of 49.
            The jackpot amount also varies based on ticket sales, similar to the 6/45 game.
[4] 6/55 -  Players draw six numbers from a pool of 55.
            The jackpot amount varies based on ticket sales,
            making it more challenging to win compared to the previous games. 
[5] 6/58 -  Players draw six numbers from a pool of 58.
            The jackpot amount varies based on ticket sales, making it the most challenging game to win. 

[0] Back
            """)
            gamemode = int(input("Please select the number of gamemode (1-5): "))
            print("-"*30)
            if gamemode == 0:
                menu()
            elif gamemode == 1:
                return 42
            elif gamemode == 2:
                return 45
            elif gamemode == 3:
                return 49
            elif gamemode == 4:
                return 55
            elif gamemode == 5:
                return 58
            else:
                print("Choose from 1 to 5 only.")
        except ValueError:
            print("-"*30)  
            print("Input a valid number.")
            print("-"*30)

# Game Instruction
def instruction():
    print("""
How to Play?:
1. Choose a gamemode.
2. Enter 6 different numbers.
    2a. If you don't want to pick a number,
        enter the command for LUCKY PICK and the system will choose a number for you.
    2b. If you want to cancel your ticket,
        enter the command for VOID and the system will disregard your ticket.
3. The system will generate winning numbers.
4. If your numbers match, you win!

(Winner prizes vary depending on gamemodes.)
""")
    return menu()