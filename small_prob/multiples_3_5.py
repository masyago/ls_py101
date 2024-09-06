def multisum(target_number):
    result = 0
    for number in range(1, target_number + 1):
        if (number % 3 == 0 or number % 5 == 0):
            result += number
    return result
    
# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)