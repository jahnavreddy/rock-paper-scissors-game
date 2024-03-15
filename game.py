import random

OPTIONS = ['rock', 'paper', 'scissors']

def get_points():
    value = int(input("Enter the number of points you want to play: "))
    return value

def user_choice():
    choice = input("Enter your choice: Rock, Paper, or Scissors: ").lower()
    while choice not in OPTIONS:
        print("Invalid option!")
        choice = input("Enter your choice: Rock, Paper, or Scissors: ").lower()
    return choice

def computer_choice():
    choice = random.choice(OPTIONS)
    return choice

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Instructions: Enter 'rock', 'paper', or 'scissors'.")
    user_points = 0
    computer_points = 0
    max_points = get_points()
    
    while user_points != max_points and computer_points != max_points:
        user = user_choice()
        computer = computer_choice()
        
        print('Computer chose:', computer)
        
        if (
            (user == 'rock' and computer == 'scissors') or
            (user == 'paper' and computer == 'rock') or
            (user == 'scissors' and computer == 'paper')
        ):
            user_points += 1
            print('You earned a point!')
        elif user == computer:
            print('No points awarded. It\'s a tie!')
        else:
            computer_points += 1
            print('Computer earned a point!')
        
        print(f"Points - Computer: {computer_points}, Your points: {user_points}")
    
    if user_points == max_points:
        print('Congratulations! You win!')
    else:
        print('Sorry, Computer wins!')

if __name__ == "__main__":
    play_game()
