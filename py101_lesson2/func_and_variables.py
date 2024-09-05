# EX1
# my_var = 1

# def my_func():
#     print(my_var) # Output: 1

# my_func()


# # EX2
# my_var = 1      #id 1

# def my_func():
#     my_var = 2  #id 2

# my_func()
# print(my_var)  # Output: 1. id 1

#EX3
# my_var = [1]   #id 1

# def my_func():
#     my_var[0] = 2  #id 1

# my_func()
# print(my_var)  # Output: [2]. #id 1

#EX4
# def my_func():
#     my_var = 1

# my_func()
# print(my_var)  # NameError: name 'my_var' is not defined

#EX5
# my_var = [1]    #id 1

# def my_func(my_var):
#     my_var.append(2)    #id 1

# my_func(my_var)
# print(my_var)  # Output: [1, 2] #id 1

#EX6
# my_var = [1]      #id 1

# def my_func(my_var):
#     my_var = [2]       #id 2

# my_func(my_var)
# print(my_var)  # Output: [1]. id 1


# EX7
# my_var = "Hello"    #id 1

# def my_func():
#     print(my_var + " world")  # Output: "Hello world"   #id 1

# my_func()

#EX8
# my_var = "Hello"      # id 1

# def my_func():
#     return my_var + " world"   #id 1

# my_func()     # the code does not capture the return value. WHY?
# print(my_var) # Output: "Hello"

#EX9
my_var = "Hello"       #id 1

def my_func():
    my_var = my_var + " world"   #id 2
    # UnboundLocalError: local variable 'my_var' referenced before assignment
    return my_var

my_func()
print(my_var)     