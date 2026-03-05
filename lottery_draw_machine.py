import random

total_draws = 6
max_ball_number = int(input("max: "))

def winner_ticket(total_draws, max_ball_number):
    lucky_ticket = random.sample(range(1, max_ball_number + 1), total_draws)
    return sorted(lucky_ticket)

def user_ticket(total_draws, max_ball_number):
    user_bets = []
    while len(user_bet) < total_draws:
        try:
            bet = int(input(f"Bet Number {len(user_bet) + 1}: "))
            if bet > max_ball_number:
                print(f"Your bet must be between 1 and {max_ball_number}")
            elif bet in user_bets:
                print(f"You've already bet that number.")
            else:
                user_bets.append(bet)
        except ValueError:
            print("Invalid input. Please enter a number.")

#-----MAIN-----
if __name__ == "__main__":
    print("WELCOME TO LOTTERY DRAW MACHINE\n")

print("""
Instructions:
            



""")

user_bet = user_ticket(total_draws, max_ball_number)
lucky_ticket = winner_ticket(total_draws, max_ball_number)

print(f"{user_bet}\n")
print(f"{lucky_ticket}")