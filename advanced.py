import random

def is_win(player, opponent):
    # return true if player wins
    # r>s, s>p, p>r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

u = 0
c = 0

while True:
    user = input("Enter your choice: rock(r)/paper(p)/scissors(s)\n").lower()
    computer = random.choice(['r','p','s'])

    if user == computer:
       print(f"\nIt's a tie, computer also showed {computer}")
       print(f"\nCurrent Points\nYou - {u}\nComputer - {c}")

    # r>s, s>p, p>r

    elif is_win(user, computer):
        u = u + 1
        print(f"\nYou got a point! Computer showed {computer}.")
        print(f"\nCurrent Points\nYou - {u}\nComputer - {c}")
    
    else:
        c = c + 1
        print(f"\nOh! Computer showed {computer}. Computer gets a point")
        print(f"\nCurrent Points\nYou - {u}\nComputer - {c}")

    play_again = input("\nPlay again? (y/n): ")
    if play_again.lower() != "y":
        if c>u:
            print(f"\nGame ends, Computer won! {c} - {u}")
        elif u>c:
            print(f"\nGame ends, You won! {u} - {c}")
        else:
            print(f"\nGame ends in a tie!! {u} - {c}")
        break



    
