import random
def play():
    user = input("What is your choice? 'r' for rock, 's' for scissors, 'p' for paper\n")
    computer = random.choice (['r', 's', 'p'])

    if user == computer:
        return "It's a tie"
    # r > s, s > p, p > r
    if is_win (user, computer):
       return "You won!"

def is_win(player, opponent):
    # return True if player wins
    # r > s, s > p, p > r
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p")\
        or (player == "p" and opponent == "r"):
        return True

print(play())
