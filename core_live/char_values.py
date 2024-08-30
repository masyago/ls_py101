# # Write a function that accepts an alphabetical character and returns
# the 'value' of that character.

# The 'value' is relative to where the letter appears in the alphabet.
# 'a' is 1, 'b' is 2, 'B' is 2, etc...
# For invalid inputs, return `None`. 
#### Bonus Question ####
# What assumptions did you have to make in order to write this function?


# convert letters to upper case
# Use ASCII codes ex A code is 65. formula for the value (ASCII code - 64)
# return None if input outside of ASCII range


def letter_to_number():
    print("Type one letter")
    char = input()
    char = char.upper()
    char_ascii_code = ord(char)
    if char_ascii_code >= 65 and char_ascii_code <= 90:
        char_value = char_ascii_code - 64
        return char_value
    else:
       return None

print(letter_to_number())

# Assumptions: that we will have only one character as an input