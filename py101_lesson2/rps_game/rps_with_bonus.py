import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'Spock']
SHORT_VALID_CHOICES = ['r', 'p', 's', 'l', 'k']

def prompt(message):
    print(f'==> {message}')
    
def display_choice_options():           # tyoe ch to remind choice options
    choices_words_letters = dict(zip(SHORT_VALID_CHOICES, VALID_CHOICES))
    prompt('You can use one letter codes:')
    for key, value in choices_words_letters.items():
        print(f'{key} for {value}')
# def remind_rules: type rr to remind rules
# def display_rules:
def display_winner(player, computer):
    global winner
    prompt(f'You chose {user_choice}, computer chose {computer_choice}')
    
    if (((player == 'rock' or player == 'r') and (computer == 'scissors' or computer == 'lizard')) or
        ((player == 'paper' or player == 'p') and (computer == 'rock' or computer == 'Spock')) or
        ((player == 'scissors' or player == 's') and (computer == 'paper' or computer == 'lizard')) or
        ((player == 'Spock' or player == 'k') and (computer == 'scissors' or computer == 'rock')) or
        ((player == 'lizard' or player == 'l') and (computer == 'paper' or computer == 'Spock'))):
            winner = 'Player'
            print("You won!")
    elif (((player == 'rock' or player == 'r') and (computer == 'paper' or computer == 'Spock')) or
         ((player == 'paper' or player == 'p') and (computer == 'scissors' or computer == 'lizard')) or
         ((player == 'scissors' or player == 's') and (computer == 'Spock' or computer == 'rock')) or
         ((player == 'Spock' or player == 'k') and (computer == 'lizard' or computer == 'paper')) or
         ((player == 'lizard' or player == 'l') and (computer == 'rock' or computer == 'scissors'))):
             winner = 'Computer'
             print("Computer won!")
    else:
        winner = 'Nobody'
        print("It's a tie")
        
# def count_score():
#     global winner
#     score = {
#         'player' : 0,
#         'computer' : 0
#     }
#     while (score['player'] and score['computer']) < 3:
#         if winner == 'Player':
#             score['player'] += 1
#         elif winner == 'Computer':
#             score['computer'] += 1
    
#     print(score)
    
print("Let's play rock, paper, scissors, spock, lizard. Rules: ")

score = {
    'player' : 0,
    'computer' : 0
}

while True:
    prompt(f"Choose one: {', '.join(VALID_CHOICES)}")      #add join/concat valid_choices and short_valid choces like this: rock (r), Spock (k)
    display_choice_options()
    user_choice = input("You choose: ")
    # add clean_inout function and initialize user_choice_clean

    while user_choice not in (VALID_CHOICES + SHORT_VALID_CHOICES):
        prompt("That's not a valid choice")
        user_choice = input()
    
    computer_choice = random.choice(VALID_CHOICES)
    winner = ''
    display_winner(user_choice, computer_choice)
    print(f"This round's winner is {winner}")
    
    

    # while (score['player'] and score['computer']) < 3:
        if winner == 'Player':
            score['player'] += 1
        elif winner == 'Computer':
            score['computer'] += 1
        
        print(score)
        
    while True:
        prompt('Do you want to play again?')
        answer = input().lower()
    
        if answer.startswith('n') or answer.startswith('y'):
            break
        else:
            prompt("That's not a valid choice")
    
    if answer[0] == 'n':
        break
    