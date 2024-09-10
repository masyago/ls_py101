# def greetings(name_lst, job_dict):
#     full_name = (' ').join(name_lst)

#     job = ''
#     for key in job_dict:
#         job += job_dict[key] + ' '
    
#     greeting = "Hello, " + full_name + '! Nice to have a ' + job + 'around.'
#     print(greeting)

# greeting = greetings(
#     ["John", "Q", "Doe"],
#     {"title": "Master", "occupation": "Plumber"},
# )

# Using f-string

def greetings(name_lst, job_dict):
    return(f"Hello, {(' ').join(name_lst)}! Nice to have a {job_dict['title']}"
           f" {job_dict['occupation']} around.")
    
greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)

print(greeting)