import random


def winner_ticket(total_draws=6, max_balls=49):
    lucky_ticket = random.sample(range(1, max_balls + 1), total_draws)
    return sorted(lucky_ticket)

lucky_ticket = winner_ticket()

if __name__ == "__main__":
    print("WELCOME TO LOTTERY DRAW MACHINE\n")
