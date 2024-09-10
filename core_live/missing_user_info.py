# Write a function that, given user info that may be `None`, populates
# any missing info using short-circuiting logic.

def normalize(name, age, email):
    user_info = {}
    # if (name != None) and (age != None) and (email != None):
    #     user_info = {"name" : name,
    #                  "age" : age,
    #                  "email" : email
    #     }
    #     return user_info
    if name == None or age == None or email == None:
        user_info[_] = "Unknown"
        return user_info
    

print(normalize('Marcy', 10, "e@gmail.com"))
print(normalize('Marcy', None, None))
# # {"name": "Marcy", "age": "Unknown", "email": "Unknown"}
print(normalize(None, None, 'best.user@gmail.com'))
# {"name": "Jane Doe", "age": "Unknown", "email": "best.user@gmail.com"}

## Bonus Challenge ##
# What happens if we pass in an empty string as the `name` or `email`?
# How might we improve our function to replace these with `"unknown"`?
# What if we pass in a negative number for the `age`?
# Can you make these improvements while still using short-circuiting?