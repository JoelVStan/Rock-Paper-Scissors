import random

def play():
    user_points = 0
    computer_points = 0

    max_points = int(input("Enter the maximum points:"))
    while user_points <= max_points or computer_points <= max_points:
        user = input("Enter yourn choice: rock/paper/scissors\n").lower()
        computer = random.choice(['rock','paper','scissors'])

        if user == computer:
            result = f"\nIt's a tie, computer showed {computer}"
            return result

        # r>s, s>p, p>r

        if is_win(user, computer):
            result = f"\nYou won, computer showed {computer}"
            user_points+=1
            return result
    
        computer_points +=1
        return f"\nYou lost, computer showed {computer}"
    

def is_win(player, opponent):
    # return true if player wins
    # r>s, s>p, p>r
    if (player == 'rock' and opponent == 'scissors') or (player == 'scissors' and opponent == 'paper') or (player == 'paper' and opponent == 'rock'):
        return True

if __name__ == '__main__':

    print(play())