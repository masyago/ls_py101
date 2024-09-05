# Write a function that takes two strings as arguments, determines the length of 
# the two strings, and then returns the result of concatenating the shorter string,
# the longer string, and the shorter string once again. You may assume that the
# strings are of different lengths.

# These examples should all print True
# print(short_long_short('abc', 'defgh') == "abcdefghabc")
# print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
# print(short_long_short('', 'xyz') == "xyz")

def short_long_short(str1, str2):
    result_str = str()
    
    str1_len = len(str1)
    str2_len = len(str2)
    
    if str1_len < str2_len:
        result_str = result_str + str1 + str2 + str1
    elif str1_len > str2_len:
        result_str = result_str + str2 + str1 + str2
    else:
        print('The strings are the same length')

    return result_str
    
str1 = input('Enter first string\n')
str2 = input('Enter second string\n')

print(short_long_short(str1, str2))

These examples should all print True
print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")


# More concise version
# def concise_short_long_short(str1, str2):
#     if len(str1) < len(str2):
#         return (str1 + str2 +str1)
#     elif len(str1) > len(str2):
#         return (str2 + str1 + str2)
        
# print(concise_short_long_short(str1, str2))