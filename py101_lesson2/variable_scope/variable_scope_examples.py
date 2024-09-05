# name = 'John'

# def greet():
#     print(f"Hello, {name}!")

# greet()  # Output: Hello, John!


# Rule 1: Variables defined in a function are local to that function and cannot 
# be accessed in the outer scope.

# def my_func():
#     local_var = 10
#     print(local_var)

# my_func()  # Output: 10
# print(local_var)  # Raises NameError: name 'local_var' is not defined

# Rule 2:Variables that are defined within a function are local unless explicitly
# marked as global or nonlocal

# def my_func():
#     global global_var
#     global_var = 20

# my_func()
# print(global_var) # Output: 20

# Rule 3: Variables used but not reassigned in a function may be in the outer scope

# outer_var = 15

# def my_func():
#     print(outer_var)

# my_func()  # Output: 15


# Rule 4: Peer scopes do not conflict

# def func_a():
#     a = 'hello'
#     print(a)

# def func_b():
#     print(a)  # NameError: name 'a' is not defined

# func_a()
# func_b()

# Rule 5: Nested functions have their own scope

a = 1  # first level variable

def foo():  # second level
    b = 2

    def bar():  # third level
        c = 3
        print(a)  # => 1
        print(b)  # => 2
        print(c)  # => 3

    bar()

    print(a)  # => 1
    print(b)  # => 2
    print(c)  # => NameError: name 'c' is not defined

foo()