import random

def play():

    user = input("Enter yourn choice: 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'tie'

    # r>s, s>p, p>r

    if is_win(user, computer):
        return 'You Won!'
    
    return 'You Lost!'


def is_win(player, opponent):
    # return true if player wins
    # r>s, s>p, p>r
    if (player == 'r' and opponent == 's') and (player == 's' and opponent == 'p') and (player == 'p' and opponent == 'r'):
        return True

print(play())