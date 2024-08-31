# COERCING TO INTEGERS

# integer_str = "42"
# integer = int(integer_str)
# print(integer)             # Output 42

# non_numeric_str = "abc"
# # non_numeric_integer = int(non_numeric_str)
# # print(non_numeric_integer)                   # ValueError: invalid literal for int() with base 10: 'abc'
# try:
#     non_numeric_integer = int(non_numeric_str)
# except ValueError:
#     print("Cannot convert to int")

# true_number = int(True)
# print(true_number)

# false_number = int(False)
# print(false_number)

# float_number = int(4.36)
# print(float_number)


# list_example = []
# list_number = int(list_example)
# print(list_number)

#  COERCING TO FLOATS

# float_str = "3.14"
# float_number = float(float_str)
# print(float_number)              # Output 3.14

# result = float('inf') - float('inf')
# print(result) # nan


# COERCING TO FLOAT
# print(str(True))    #True
# print(str([1, 2]))

# repr() function retruns a string representation of an object
x = [1, 2, 3]
test = repr(x)
print(test)