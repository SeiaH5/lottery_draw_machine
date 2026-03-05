import random
import lottery_login
import lottery_menu

#Lottery drawing
class lottery_drawing:
    @staticmethod
    def winner_ticket(total_draws, max_ball_number):
        lucky_ticket = random.sample(range(1, max_ball_number + 1), total_draws)
        return sorted(lucky_ticket)

    @staticmethod
    def add_ticket(total_draws, max_ball_number):
        user_bets = []
        print("""
[L] Lucky Pick
[V] Void
        """)
        while len(user_bets) < total_draws:
            try:
                bet = input(f"Bet Number {len(user_bets) + 1}: ")
                if bet.upper() == "L":
                    user_bets.append(random.randrange(1, max_ball_number + 1))
                elif bet.upper() == "V":
                    print("Your draw has been voided.")
                    break
                
                elif int(bet) > max_ball_number or int(bet) < 1:
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
    lottery_login.front_panel()
    while True:    
        lottery_menu.menu()
        total_draws = 6
        max_ball_number = lottery_menu.gamemode()
        ticket = lottery_drawing.add_ticket(total_draws, max_ball_number)
        drawn_ticket = lottery_drawing.winner_ticket(total_draws, max_ball_number)
        print(f"\n{ticket}\n")
        print(f"{drawn_ticket}")
        continue


if __name__ == "__main__":
    print("WELCOME TO LOTTERY DRAW MACHINE")
    main()


