import random

#Gamemode selector
def gamemode():
    gamemode = []
    while gamemode != range(0,5):
        try:
            gamemode = int(input("Please select the number of gamemode: "))
            if gamemode == 1:
                max_ball_number = 42
                return max_ball_number
            elif gamemode == 2:
                max_ball_number = 45
                return max_ball_number
            elif gamemode == 3:
                max_ball_number = 49
                return max_ball_number
            elif gamemode == 4:
                max_ball_number = 55
                return max_ball_number
            elif gamemode == 5:
                max_ball_number = 58
                return max_ball_number
            else:
                print("Choose from 1 to 5 only.")
        except ValueError:
                print("Input a valid number.")

#Random number generator
def winner_ticket(total_draws, max_ball_number):
    lucky_ticket = random.sample(range(1, max_ball_number + 1), total_draws)
    return sorted(lucky_ticket)

#User bet input
def user_ticket(total_draws, max_ball_number):
    user_bets = []
    while len(user_bets) < total_draws:
        try:
            bet = int(input(f"Bet Number {len(user_bets) + 1}: "))
            if bet > max_ball_number:
                print(f"Your number must be from 1 to {max_ball_number}")
            elif bet in user_bets:
                print(f"You've already bet that number.")
            else:
                user_bets.append(bet)
        except ValueError:
            print("Invalid input. Please enter a number.")

#-----MAIN-----
if __name__ == "__main__":
    print("     WELCOME TO LOTTERY DRAW MACHINE     ")

print("""
        MENU
    
    [P] Play
    [I] Instruction
""")

menu = input(
"""--------------------             
Select menu: 
""")



total_draws = 6
max_ball_number = gamemode()

user_bet = user_ticket(total_draws, max_ball_number)
lucky_ticket = winner_ticket(total_draws, max_ball_number)

print(f"{user_bet}\n")
print(f"{lucky_ticket}")