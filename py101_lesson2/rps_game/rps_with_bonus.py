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
    prompt(f'Choose one: {choice_options()}.\n'
           f'    You can type either a word or a corresponding letter')

def clean():
    if user_choice.strip().lower() == 'spock':
        return 'Spock'

    return user_choice.strip().lower()

def match_word():
    if user_choice_clean in VALID_WORDS:
        return user_choice_clean
    if user_choice_clean in VALID_LETTERS:
        chosen_index = VALID_LETTERS.index(user_choice_clean)
        return VALID_WORDS[chosen_index]

def display_choices():
    print(f'\n   You chose {user_choice_word}, computer chose {computer_choice}')

def display_winner(player, computer):
    if (((player == 'rock') and (computer in ('scissors', 'lizard'))) or
       ((player == 'paper') and (computer in ('rock', 'Spock'))) or
       ((player == 'scissors') and (computer in ('paper', 'lizard'))) or
       ((player == 'Spock') and (computer in ('scissors', 'rock'))) or
       ((player == 'lizard') and (computer in ('paper', 'Spock')))):
        winner = 'player'
        print(messages["player_won_round"])
    elif (((player == 'rock') and (computer in ('paper', 'Spock'))) or
         ((player == 'paper') and (computer in ('scissors', 'lizard'))) or
         ((player == 'scissors') and (computer in ('Spock', 'rock'))) or
         ((player == 'Spock') and (computer in ('lizard', 'paper'))) or
         ((player == 'lizard') and (computer in ('rock', 'scissors')))):
        winner = 'computer'
        print(messages["computer_won_round"])
    else:
        winner = 'nobody'
        print(messages["tie"])

    return winner

def count_score():
    if winner == 'player':
        score['player'] += 1
    elif winner == 'computer':
        score['computer'] += 1
    return score

def display_score():
    count_score()
    print(f"\n   ---------------------------"
          f"\n        Score: {score['player']} : {score['computer']}"
          f"\n   ---------------------------\n") 

def display_game_winner():
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

    score = {
     'player' : 0,
     'computer' : 0
    }

    display_game_rules()

    while True:
        display_choice_options()
        user_choice = input()

        while clean() not in (VALID_WORDS + VALID_LETTERS):
            prompt(messages["not_valid"])
            user_choice = input()

        # Convert user input to words
        user_choice_clean = clean()
        user_choice_word = match_word()

        computer_choice = random.choice(VALID_WORDS)

        display_choices()
        winner = display_winner(user_choice_word, computer_choice)
        display_score()

        if (score['player'] != 3) and (score['computer'] != 3):
            continue
        display_game_winner()
        break

    while True:
        ask_play_again()
        again = input().strip().lower()

        if again.startswith('n') or again.startswith('y'):
            os.system('clear')
            break
        not_valid()

    if again[0] == 'n':
        break
