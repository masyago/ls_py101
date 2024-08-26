# PROGRAM 1: A function that returns the sum of two numbers
# Ask user to input two numbers
# Set variables number 1 and number 2 to the inputs from user
# Convert inputs to integers, sums them
# Return the sum

# START

# GET number1
# GET number 2 
# SET result = number1 converted to interger + number 2 converted to integer
# PRINT result

# PROGRAM 2: A function that takes a list of strings, and returns a string that is all those strings concatenated together
# Iterate through the strings one by one:
#     set an empty string as a starting concatinated string
#     for each iteration, concatenate current string to string resulted in previous iteration
#     stop when there are no more strings left in the list of strings
#     Return and save the value

# START

# SET iterator = 1
# SET longString = empty string

# WHILE iterator <= length of given list
#     longString = longString + string at space 'iterator'
#     iterator = iterator + 1
    
# PRINT longString
# END

# PROBLEM 3: a function that takes a list of integers, and returns a new list 
# with every other element from the original list, starting with the first element.

# Set a new empty list 
# Iterate through the given list 
# For even indexes, Add elements of orgiinal list to the new list
# Save and print new list

#START
# SET newList = []
# SET iterator = 0
# WHILE  iterator <= len(originalList)
#     if iterator even number:
#         newList = newList with number at the space 'iterator'
# PRINT newList
# END


# # PROBLEM 4: a function that determines the index of the 3rd occurrence of a 
# given character in a string. For instance, if the given character is 'x' and the
# string is 'axbxcdxex', the function should return 6 (the index of the 3rd 'x').
# If the given character does not occur at least 3 times, return None.

# Set occurance variable to 0 
# Set index3 to 0
# go through the string statting from index 0
# If target character present, assign index3 to the index of the character and
# add 1 to the occurance variable
# Repeat while occurance equals 3
# If occurance never gets to 3 print 'None'
# Save and print index3

# START

# SET occurance = 0
# SET index3 = 0
# SET iterator = 0
# WHILE iteration <= len(givenString) and occurance <=3
#     IF character is targetCharacter
#         index3 = iterator of the character
#         occurance = occurance + 1
# IF occurance = 3
#     PRINT index3
# ELSE 
#     PRINT 'None'
    
# END

# PROBLEM 5: a function that takes two lists of numbers and returns the result
# of merging the lists. The elements of the first list should become the elements
# at the even indexes of the returned list, while the elements of the second list 
# should become the elements at the odd indexes.

# SET newList
# For index number, add element at space 'index' from list1 to newList, then 
# add elemnt at space 'index' from list2 to newList
# Until run out of elements in list1
# Save and print newList

# START
# GIVEN list1
# GIVEN list2
# SET newList

# WHILE index <= len(list1)
#     newList append element from list1 at space 'index'
#     newList append element from list2 at space 'index'
# PRINT newList

# END

