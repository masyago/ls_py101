# Write a function that takes one integer argument and returns True when the 
# number's absolute value is odd, False otherwise.

# def check_odd_number():
#     number_input = input()
#     number = int(number_input)
#     if number % 2 == 1:
#         return True
#     else:
#         return False
        
# print(check_odd_number())


# LS solution
def is_odd(number):
    return abs(number) % 2 == 1      # abs function returns the absolute value of the argument
                                     # % check for modulo
    
print(is_odd(5))