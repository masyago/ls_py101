'''
Mortgage calculator that calculates monthly payments. 
'''

import json
from os import system

with open('messages.json', 'r') as file:
    messages = json.load(file)

def prompt(message):
    print(f'\n==> {message}')

def validate_loan_input(number_str):
    number_str_clean = number_str.replace(',', '').replace('$', '')
    while True:
        try:
            number = float(number_str_clean)
            if number > 0:
                break
            return True
        except ValueError:
            return True
    return False

def validate_apr_input(number_str):
    number_str_clean = number_str.replace('%','')
    while True:
        try:
            number = float(number_str_clean)
            if number >= 0:
                break
            return True
        except ValueError:
            return True
    return False

def validate_duration(number_str):
    while True:
        try:
            number = float(number_str)
            if number > 0:
                break
            return True
        except ValueError:
            return True
    return False

# Clear screen
system('clear')

print(messages["greeting"])

def calc_main():
    print(messages["loan_header"])

    # Get loan amount and check if number is valid
    prompt(messages["loan_amount"])
    get_loan_amount = input()
    while validate_loan_input(get_loan_amount):
        prompt(messages["invalid_loan_amount"])
        get_loan_amount = input()
    loan_amount_clean = get_loan_amount.replace(',', '').replace('$', '')

    # Get APR and check if number is valid
    prompt(messages["apr"])
    get_apr = input()
    while validate_apr_input(get_apr):
        prompt(messages["invalid_apr"])
        get_apr = input()
    apr_clean = get_apr.replace('%', '')

     # Get loan duration and check if number is valid
    prompt(messages["loan_term"])
    get_duration_years = input()
    while validate_duration(get_duration_years):
        prompt(messages["invalid_duration"])
        get_duration_years = input()

    # Convert inputs to floats
    loan_amount = float(loan_amount_clean)
    apr = float(apr_clean)
    duration_years = float(get_duration_years)

    # Calculate values for monthly_payment formula
    duration_months = duration_years * 12
    monthly_interest_rate = apr / 12 / 100

    # Calculate montly payment and print out summary
    if monthly_interest_rate == 0:
        monthly_payment = loan_amount / duration_months
    else:
        monthly_payment = (loan_amount * (monthly_interest_rate
                          / (1 - (1 + monthly_interest_rate)
                          ** (-duration_months))))
    rounded_monthly_payment = round(monthly_payment, 2)
    print(messages["result_header"])
    print(f'LOAN DETAILS\n'
          f'Loan amount: ${loan_amount}\n'
          f'APR: {apr}%\n'
          f'Loan term: {duration_years} years\n'
          f'\nMONTHLY PAYMENT: ${rounded_monthly_payment:,}\n'
          f'========================')

    def calc_continue():
        print(messages["continue_request"])
        response = input()
        response_clean = response.lower().strip()
        match response_clean:
            case "y":
                calc_main()
            case "n":
                print(messages["end"])
                exit()
            case _:
                print(messages["y_or_n"])
                calc_continue()

    calc_continue()

calc_main()
