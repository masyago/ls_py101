import json
import os
import random

VALID_WORDS = ['rock', 'paper', 'scissors', 'lizard', 'Spock']
VALID_LETTERS = ['r', 'p', 's', 'l', 'k']

with open('rpssl_messages.json', 'r') as file:
    messages = json.load(file)
    
def prompt(message):
    print(f'\n==> {message}')
    
def display_game_rules():
    print(messages["welcome"])
    print('''
    ---------------------------
    The rules are: 
    - Scissors cut paper
    - Paper covers rock
    - Rock crushes lizard
    - Lizard poisons Spock
    - Spock smashes scissors
    - Scissors decapitate lizard
    - Lizard eats paper
    - Paper disproves Spock
    - Spock vaporizes rock
    - Rock crushes scissors
    
    The player who gets 3 points first wins the game.
    ----------------------------
    LET'S PLAY!
    ----------------------------''')
    
def choice_options():          
    valid_choices = ''
    for words in VALID_WORDS:
        for letters in VALID_LETTERS:
            if VALID_WORDS.index(words) == VALID_LETTERS.index(letters):
                options = words + '(' + letters + ')' + ', '
                valid_choices += options
    valid_choices = valid_choices[:-2]
    return valid_choices
    
def display_choice_options():
    prompt(f'Choose one: {choice_options()}')
    
def clean_input(user_choice):
    user_choice = user_choice.strip()
    if user_choice.lower() == 'spock':
        user_choice_clean = 'Spock'
    else:
        user_choice_clean = user_choice.lower()

    return user_choice_clean

def match_word(user_choice_clean):
    if user_choice_clean in VALID_WORDS:
        user_choice_word = user_choice_clean
    elif user_choice_clean in VALID_LETTERS:
        chosen_index = VALID_LETTERS.index(user_choice_clean)
        user_choice_word = VALID_WORDS[chosen_index]
        
    return user_choice_word
        
def display_choices(player, computer):
    print(f'\n   You chose {user_choice_word}, computer chose {computer_choice}')


def display_winner(player, computer):
    if (((player == 'rock') and (computer == 'scissors' or computer == 'lizard')) or
        ((player == 'paper') and (computer == 'rock' or computer == 'Spock')) or
        ((player == 'scissors') and (computer == 'paper' or computer == 'lizard')) or
        ((player == 'Spock') and (computer == 'scissors' or computer == 'rock')) or
        ((player == 'lizard') and (computer == 'paper' or computer == 'Spock'))):
            winner = 'player'
            print(messages["player_won_round"])
    elif (((player == 'rock') and (computer == 'paper' or computer == 'Spock')) or
         ((player == 'paper') and (computer == 'scissors' or computer == 'lizard')) or
         ((player == 'scissors') and (computer == 'Spock' or computer == 'rock')) or
         ((player == 'Spock') and (computer == 'lizard' or computer == 'paper')) or
         ((player == 'lizard') and (computer == 'rock' or computer == 'scissors'))):
             winner = 'computer'
             print(messages["computer_won_round"])
    else:
        winner = 'nobody'
        print(messages["tie"])
    return winner 
    
def count_score(winner):
    if winner == 'player':
        score['player'] += 1
    elif winner == 'computer':
        score['computer'] += 1
    return score
    
def display_score(score):
    count_score(winner)
    print(f"\n   ---------------------------"
          f"\n        Score: {score['player']} : {score['computer']}"
          f"\n   ---------------------------\n") 
    
def display_game_winner(score):
    if score['player'] == 3:
        print(messages["player_won_game"])
    elif score['computer'] == 3:
        print(messages["computer_won_game"])
        
def ask_play_again():
    prompt(messages["play_again"])

def not_valid():
    prompt(messages["not_valid"])
    
# Main loop
while True:
    os.system('clear')
    
    display_game_rules()
    
    score = {
         'player' : 0,
         'computer' : 0
        }
        
    while True:
        winner = ''
        display_choice_options()

        user_choice = input()

        while clean_input(user_choice) not in (VALID_WORDS + VALID_LETTERS):
            prompt(messages["not_valid"])
            user_choice = input()
            
        
        # Convert user input to words
        user_choice_clean = clean_input(user_choice)
        user_choice_word = match_word(user_choice_clean)
        
        computer_choice = random.choice(VALID_WORDS)
        
        
        display_choices(user_choice_word, computer_choice)
        winner = display_winner(user_choice_word, computer_choice)
        display_score(score)
        
        if (score['player'] != 3) and (score['computer'] != 3):
            continue
        else:
            display_game_winner(score)
            break
        
    while True:
        ask_play_again()
        again = input().strip().lower()
    
        if again.startswith('n') or again.startswith('y'):
            os.system('clear')
            break
        else:
            not_valid()
    
    if again[0] == 'n':
        break
    