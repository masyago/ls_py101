import random

VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(message):
    print(f'==> {message}')
    
def display_winner(player, computer):
    prompt(f'You chose {user_choice}, computer chose {computer_choice}')
    
    if ((player == 'rock' and computer == 'scissors') or
           (player == 'paper' and computer == 'rock') or
           (player == 'scissors' and computer == 'paper')):
        print("You won!")
    elif ((player == 'rock' and computer == 'paper') or
          (player == 'paper' and computer == 'scissors') or
          (player == 'scissors' and computer == 'rock')):
        print("Computer won!")
    else:
        print("It's a tie")
    
while True:
    prompt(f"Choose one: {', '.join(VALID_CHOICES)}")
    user_choice = input()

    while user_choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        user_choice = input()
    
    computer_choice = random.choice(VALID_CHOICES)
    
    display_winner(user_choice, computer_choice)
        
    while True:
        prompt('Do you want to play again?')
        answer = input().lower()
    
        if answer.startswith('n') or answer.startswith('y'):
            break
        else:
            prompt("That's not a valid choice")
    
    if answer[0] == 'n':
        break
    
    
