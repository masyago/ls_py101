#JSON configuration file set up
import json

with open('data.json', 'r') as file: # Open the JSON file for reading
    data = json.load(file)
    



def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False


prompt(data["start"]) # Accessing message by key


def calc_main():
    prompt(data["first_number"])
    number1 = input()


    while invalid_number(number1):
        prompt(data["invalid_number"])
        number1 = input()
    
    prompt(data["second_number"])
    number2 = input()
    
    while invalid_number(number2):
        prompt(data["invalid_number"])
        number2 = input()
    
    prompt(data["operation_prompt"])
    operation = input()
    
    while operation not in ["1", "2", "3", "4"]:
        prompt(data["invalid_prompt"])
        operation = input()
    
    
    match operation:
        case '1':   # '1' represents addition
            output = int(number1) + int(number2)
        case '2': # '2' represents subtraction
            output = int(number1) - int(number2)
        case '3': # '3' represents multiplication
            output = int(number1) * int(number2)
        case '4': # '4' represents division
            output = int(number1) / int(number2)
    
    print(f'The result is {output}.')

    def calc_continue():
        print(data["continue_request"])
        response = input()
        match response:
            case "y":
                calc_main()
            case "n":
                print(data["end"])
                exit()
            case _:
                print(data["y_or_n"])
                calc_continue()
                
    calc_continue()

    
calc_main()
