import random

def menu():
    menu = ["P", "I"]
    while True:
        print("""--------------------
        MENU

    [P] Play
    [I] Instruction
        """)
        menu_select = input("""--------------------
Select menu: """).upper()
        print("--------------------")
        if menu_select in menu:
            if menu_select == "P":
                break
            else:
                instruction()
        else:
            print("Invalid menu option.")

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
            print("--------------------")
            if gamemode == 0:
                main()
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
            print("Input a valid number.")

def instruction():
    print("""
Instructions:
1. Choose a gamemode.
2. Enter 6 different numbers.
3. The system will generate winning numbers.
4. If your numbers match, you win!

(Winner prizes vary depending on gamemodes.)
""")
    return

class lottery_drawing:
    @staticmethod
    def winner_ticket(total_draws, max_ball_number):
        lucky_ticket = random.sample(range(1, max_ball_number + 1), total_draws)
        return sorted(lucky_ticket)

    @staticmethod
    def user_ticket(total_draws, max_ball_number):
        user_bets = []
        while len(user_bets) < total_draws:
            try:
                bet = int(input(f"Bet Number {len(user_bets) + 1}: "))
                if bet > max_ball_number or bet < 1:
                    print(f"Your number must be from 1 to {max_ball_number}")
                elif bet in user_bets:
                    print("You've already bet that number.")
                else:
                    user_bets.append(bet)
            except ValueError:
                print("Invalid input. Please enter a number.")
        return sorted(user_bets)

# -----MAIN PROGRAM-----
def main():
    menu()
    total_draws = 6
    max_ball_number = gamemode()
    ticket = lottery_drawing.user_ticket(total_draws, max_ball_number)
    drawn_ticket = lottery_drawing.winner_ticket(total_draws, max_ball_number)
    print("\nYour Ticket:", ticket)
    print("Winning Ticket:", drawn_ticket)

if __name__ == "__main__":
    print("WELCOME TO LOTTERY DRAW MACHINE")
    main()