# Write a program that prompts the user for two positive numbers (floating-point), 
# then prints the results of the following operations on those two numbers: 
# addition, subtraction, product, quotient, floor quotient, remainder, and 
# power. Do not worry about validating the input.

def prgm_msg(message):
    print(f'==> {message}')
    
def convert_float(num):
    num = float(num)
    return num
# def print_math(operation_result, operator):
#     prgm_msg(f'{num1} {operator} {num2} = {operation_result}')
    
# def math_func(num1, num2):
#     num1_float = float(num1)
#     num2_float = float(num2)
    
#     addition = num1_float + num2_float
#     subtraction = num1_float - num2_float
#     product = num1_float * num2_float
#     quotient = num1_float / num2_float
#     floor_quotient = num1_float // num2_float
#     remainder = num1_float % num2_float
#     power = num1_float ** num2_float
#     return addition
    
#     print(f'{num1} + {num2} = {addition}')

prgm_msg("Enter the first number:")
num1 = input()

prgm_msg("Enter the second number:")
num2 = input()

num1 = convert_float(num1)
num2 = convert_float(num2)

# prgm_msg(f'{num1} + {num2} = {num1 + num2}')

# prgm_msg(f'{num1} - {num2} = {num1 - num2}')

# prgm_msg(f'{num1} * {num2} = {num1 * num2}')

# prgm_msg(f'{num1} / {num2} = {num1 / num2}')

# prgm_msg(f'{num1} // {num2} = {num1 // num2}')

# prgm_msg(f'{num1} % {num2} = {num1 % num2}')

# prgm_msg(f'{num1} ** {num2} = {num1 ** num2}')
    
    
# Solution with a helper function
def calculate(first, second, operator):
    match operator:
        case '+': 
            return first + second
        case '-':
            return first - second
        case '*': 
            return first * second
        case '/':
            return first / second
        case '//': 
            return first // second
        case '%':
            return first % second
        case '**':
            return first ** second
            

for operator in ['+', '-', '*', '/', '//', '%', '**']:
    operation = f'{num1} {operator} {num2}'
    result = calculate(num1, num2, operator)
    print(f'==> {operation} = {result}')
    