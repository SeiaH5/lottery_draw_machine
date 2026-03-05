import random
from utils import lottery_login, lottery_menu, lottery_database

#Lottery draw
class lottery_drawing:
    @staticmethod
    def winner_ticket(total_draws, max_ball_number):
        lucky_ticket = random.sample(range(1, max_ball_number + 1), total_draws)
        return sorted(lucky_ticket)

    @staticmethod
    def add_ticket(total_draws, max_ball_number):
        user_bets = []
        print("""\033[1m
[L] Lucky Pick
[V] Void
\033[0m""")
        while len(user_bets) < total_draws:
            try:
                bet = input(f"Bet Number {len(user_bets)+1}: ")
                if bet.upper() == "L":
                    user_bets.append(random.randint(1, max_ball_number))
                elif bet.upper() == "V":
                    print("\nYour draw has been voided.\n")
                    lottery_menu.menu()
                elif int(bet) < 1 or int(bet) > max_ball_number:
                    print(f"Your number must be from 1 to {max_ball_number}")
                elif int(bet) in user_bets:
                    print("You've already bet that number.")
                else:
                    user_bets.append(int(bet))
            except ValueError:
                print("\033[31mInvalid input. Please enter a number.\033[0m")
        return sorted(user_bets)

    @staticmethod
    def check_win(user_ticket, drawn_ticket):
        matches = set(user_ticket) & set(drawn_ticket)
        match_count = len(matches)
        print(f"Matching numbers: {sorted(matches)}")
        print(f"Total matched numbers: {match_count}")
        if match_count == len(drawn_ticket):
            print("\033[32mGALING! You won the lottery!\033[0m")
        elif match_count >= 3:
            print("\033[33mYou won a small prize!\033[0m")
        else:
            print("\033[31mBetter luck next time!\033[0m\n")
        return match_count

def redraw():
    while True:
        print("""
[1] Continue
[0] Menu
        """)
        try:
            redraw_option = int(input("Want to play another? "))
            if redraw_option == 1:
                print("\n"*10)
                return
            elif redraw_option == 0:
                print("\n"*20)
                lottery_menu.menu()
                return
            else:
                print("\033[31mInvalid input.\033[0m\n")
        except ValueError:
            print("\033[31mInvalid input. Enter a number.\033[0m\n")

def main():
    while True:
        total_draws = 6
        max_ball_number = lottery_menu.gamemode()
        ticket = lottery_drawing.add_ticket(total_draws, max_ball_number)
        if ticket is None:
            return
        drawn_ticket = lottery_drawing.winner_ticket(total_draws, max_ball_number)
        print(f"\nYour ticket: {ticket}")
        print(f"Winning numbers: {drawn_ticket}\n")
        match_count = lottery_drawing.check_win(ticket, drawn_ticket)

        #Save to JSON Database
        lottery_database.save_ticket(
            lottery_login.current_user,
            max_ball_number,
            ticket,
            drawn_ticket,
            match_count
        )
        redraw()

if __name__ == "__main__":
    lottery_login.front_panel()
    lottery_menu.menu()
    main()