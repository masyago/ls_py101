name = input("What is your name? ")
if name[-1] == '!':      #or name.endswith('!')
    print(f'HELLO {name.upper()} WHY ARE WE YELLING?')
else:
    print(f'Hello {name}.')touc