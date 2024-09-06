'''
Mortgage calculator that calculates monthly payments. 
'''

import json
from os import system
import sys

with open('messages.json', 'r') as file:
    messages = json.load(file)

def prompt(message):
    print(f'\n==> {message}')
    
def display_welcome_message():
    print(messages["greeting"])

def display_loan_header():
    print(messages["loan_header"])
    
def prompt_loan_amount():
    prompt(messages["loan_amount"])
    get_loan_amount = input()
    
    while valid_loan_input(get_loan_amount):
        prompt(messages["invalid_loan_amount"])
        get_loan_amount = input()
        
    loan_amount_clean = get_loan_amount.replace(',', '').replace('$', '')
    loan_amount = float(loan_amount_clean)
    return loan_amount
    
def prompt_apr():
    prompt(messages["apr"])
    get_apr = input()
    while valid_apr_input(get_apr):
        prompt(messages["invalid_apr"])
        get_apr = input()
    apr_clean = get_apr.replace('%', '')
    apr = float(apr_clean)
    return apr
    
def prompt_duration_years():
    prompt(messages["loan_term"])
    get_duration_years = input()
    while valid_duration(get_duration_years):
        prompt(messages["invalid_duration"])
        get_duration_years = input()
    duration_years = float(get_duration_years) 
    return duration_years
    
def valid_loan_input(number_str):
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

def valid_apr_input(number_str):
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

def valid_duration(number_str):
    while True:
        try:
            number = float(number_str)
            if number > 0:
                break
            return True
        except ValueError:
            return True
    return False
    
def calc_duration_months(duration_years):
    duration_months = duration_years * 12
    return duration_months
    
def calc_monthly_interest_rate(apr):
    monthly_interest_rate = apr / 12 / 100
    return monthly_interest_rate

def calc_monthly_payment(monthly_interest_rate, loan_amount, duration_months):
    if monthly_interest_rate == 0:
        monthly_payment = loan_amount / duration_months
    else:
        monthly_payment = (loan_amount * (monthly_interest_rate
                          / (1 - (1 + monthly_interest_rate)
                          ** (-duration_months))))
    return monthly_payment
    
def calc_continue():
    print(messages["continue_request"])
    response = input()
    response_clean = response.lower().strip()
    match response_clean:
        case "y":
            system('clear')
            calc_main()
        case "n":
            print(messages["end"])
            sys.exit(0)
        case _:
            print(messages["y_or_n"])
            calc_continue()
            
def display_summary(loan_amount, apr, duration_years, monthly_payment):
    print(messages["result_header"])
    print(f'LOAN DETAILS\n'
          f'Loan amount: ${loan_amount:.2f}\n'
          f'APR: {apr}%\n'
          f'Loan term: {duration_years} years\n'
          f'\nMONTHLY PAYMENT: ${monthly_payment:.2f}\n'
          f'========================')

# Clear screen
system('clear')

# Main 
def calc_main():
    display_welcome_message()
    display_loan_header()

    # Get values needed for monthly payment calculations
    loan_amount = prompt_loan_amount()
    apr = prompt_apr()
    duration_years = prompt_duration_years()
    
    
    # Calculate monthly payment and values needed for the formula
    duration_months = calc_duration_months(duration_years)
    monthly_interest_rate = calc_monthly_interest_rate(apr)
    monthly_payment = calc_monthly_payment(monthly_interest_rate, loan_amount, duration_months)

    display_summary(loan_amount, apr, duration_years, monthly_payment)
    
    calc_continue()

calc_main()
