# Write a function that takes any year greater than 0 as input and returns True 
# if the year is a leap year, or False if it is not.

# if year
# If the year is divisible by 400, it is a leap year.
# If the year is divisible by 100 but not by 400, it is not a leap year.
# If the year is divisible by 4 but not by 100, it is a leap year.
# All other years are not leap years.

def is_leap_year(year):
    if year < 1752:
        if (year % 4 == 0):
            return True
        else:
            return False
    elif year >= 1752:
        if year % 400 == 0:
            return True
        elif (year % 100 == 0):
            return False
        elif (year % 4 == 0):
            return True
        else:
            return False
        
        

# year = int(input("Let's determine if the year was a leap year. Type a year number\n"))

# print(is_leap_year(year))


# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == True)
print(is_leap_year(1100) == True)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == True)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)