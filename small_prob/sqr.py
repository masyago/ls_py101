# def square(num):
#     return num * num
    
# print(square(5) == 25)   # True
# print(square(-8) == 64)  # True


# Alternative:
# def square(number):
#     return multiply(number, number)


# Further Exploration: power to the n using multiply function

def multiply(num1, num2):
    return num1 * num2
    
def power(num, n):
    result = 1
    for i in range(1, n+1):
        result = multiply(result, num)
    return result
        
print(power(2, 2))
print(power(2, 10))