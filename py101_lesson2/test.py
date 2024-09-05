# names = ['kim', 'joe', 'sam']
# for _ in names:
#     print('Got a name!')

# Make dictionary out of 2 lists
# VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'Spock']
# SHORT_VALID_CHOICES = ['r', 'p', 's', 'l', 'k']

# # choices_words_letters = dict()

# # # for index in range(len(VALID_CHOICES)):
# # #     choices_words_letters[SHORT_VALID_CHOICES[i]] = VALID_CHOICES[i]
# # choices_words_letters = dict(zip(SHORT_VALID_CHOICES, VALID_CHOICES))
# # print('You can use one letter codes:')
# # for key, value in choices_words_letters.items():
# #     print(f'{key} for {value}')
        
# # # print(choices_words_letters)

# print(VALID_CHOICES + SHORT_VALID_CHOICES)


# total_score = {
#         'player' : 0 ;
#         'computer_score' : 0
# }
#  while (score['player'] and score['computer']) < 3:
#       if winner == 'Player':
#           score['player'] += 1
#       elif winner == 'Computer':
#              score['computer'] += 1
    

# display_scores 

# if score['player'] == 3:
#     print('You are the Grand Winner!')
# elif score['computer'] == 3:
#     print('Computer is the Grand Winner!')
         
# number = input()
# # try:
# #     int(number)
# #     if int(number) > 0:
# #         break
# #     else:
# #         print('Error: The number is not greater than zero. Please try again')
# # except ValueError:
# #     return True

# try:
#     int(number)
#     if int(number) > 0:
#         break
#     else:
#         print("number is <= 0")
# except ValueError:
#     print('Error')
# print('end')



# def get_amount():
#     while True:
#         amount = input("Enter amount: ")
#         try:
#             val = int(amount)
#             if val >= 0:
#                 break
#             else:
#                 print("Amount can't be negative, try again")
#         except ValueError:
#             print("Amount must be a number, try again")
#         return val
    
# print(get_amount())

# user_input = input("Enter a number > 0: \n")

def validate_input(user_input):
    while True:
        try:
            int(user_input)
            if int(user_input) > 0:
                break
            else:
                print("The number is not greater than zero. Try again")
                return True
        except ValueError:
            print("It's not a number. Try again")
            return True
    return False


# func1 requests input
# func2 validates input


user_input = input("Enter a number > 0: \n")

while validate_input(user_input):
    user_input = input("Enter a number > 0: \n")
    
print(f'number is {int(user_input)}')