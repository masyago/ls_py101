a = 1

def my_function():
    global a
    print(a)
    a = 2

my_function()
print(a)