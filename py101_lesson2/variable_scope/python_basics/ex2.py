x = 10     #id1

def my_function():
    global x      # id1
    x = x + 5     # id 1
    print(x)

my_function()
print(x)
