# Write a program that asks the user to enter an integer greater than 0, then asks
# whether the user wants to determine the sum or the product of all numbers
# between 1 and the entered integer, inclusive
# 
# Further Exploration:
# Suppose the input was a list of space separated integers instead of just a 
# single integer? How would your compute_sum and compute_product functions change?

def validate_number(number):
    while True:
        try:
            int(number)
            if int(number) > 0:
                break
            else:
                print('Error: The number is not greater than zero. ' 
                      'Please try again')
                return True
        except ValueError:
            print("It's not a number. Try again")
            return True
    
    return False
    
def validate_operation(operation):
    while operation.strip().lower() not in ['s','p']:
            print('Error. Please type letter "s" for sum or letter "p" for product')
            return True
    return False
    
    
def compute_sum(list_of_integers):
    sum_list = []
    for integer in list_of_integers:
        sum_is = 0
        for integer in range(1, integer + 1):   # here we could use sum(range(1, number + 1))
            sum_is += integer
        sum_list.append(sum_is)
    return sum_list

def compute_product(list_of_integers):
    product_list = []
    for integer in list_of_integers:
        product = 1
        for integer in range(1, integer + 1):
            product *= integer
        product_list.append(product)
    return product_list

print('Enter integers separated by a space. Each integer should be greater '
      'than zero')
integers = input()
list_of_strings = integers.split()
print(list_of_strings)

list_of_integers = []

for integer in list_of_strings:
    integer = int(integer)
    list_of_integers.append(integer)
    
print(list_of_integers)

# while validate_number(number):
#     number = input()
    
# number = int(number)

print('Enter "s" to compute the sum, or "p" to compute the product.')
operation = input()


# while validate_operation(operation):
#     operation = input()

if operation.strip().lower() == 's':
    compute_sum(list_of_integers)
    print(f'The sums of the integers between 1 and {list_of_integers} is {compute_sum(list_of_integers)}.')
elif operation.strip().lower() == 'p':
    compute_product(list_of_integers)
    print(f'The product of the integers between 1 and {list_of_integers} is {compute_sum(list_of_integers)}.')
else:
    print('Error: Unknown operation')