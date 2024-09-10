# def penultimate(string):
#     words_list = string.split()
#     return words_list[-2]
    
# print(penultimate("last word"))

# # These examples should print True
# print(penultimate("last word") == "last")
# print(penultimate("Launch School is great!") == "is")


# Further exploration: write a function that retrieves the middle word of
# a phrase/sentence. 
# Include edge case handling:
#     strings that contain no words 
#     just one word
#.    if sentence has even number of words

def middle(string):
    if len(string) < 1:
        print("The string is empty")
        
    words_list = string.split()
    word_amount = len(words_list)
    if word_amount == 1:
        print(words_list[0])
    elif word_amount % 2 == 1:
        print(words_list[word_amount // 2])
    elif word_amount % 2 == 0:
        print(f'The sentence {string} has even number of words.'
              f' Cannot find the middle')
    
string = '1 2 3 4'
middle(string)