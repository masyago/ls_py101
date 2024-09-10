# Implement `check_eligibility` such that we get the expected ouput.
# To be 'eligible', users must be at least 18. Users must be a member.
# If they are not a member then they must have filled out a survery.
def check_eligibility(age, is_member, completed_survey):
    if age < 18:
        print("Not Eligible!")
    elif is_member == True or completed_survey == True:
        print("Eligible!")
    elif is_member == False and completed_survey == False:
        print("Not Eligible!")

# Example usage:
# check_eligibility(20, True, False)  # "Eligible!"
# check_eligibility(17, True, True)   # "Not Eligible!"
# check_eligibility(25, False, True)  # "Eligible!"
# check_eligibility(30, False, False) # "Not Eligible!"
# check_eligibility(30, True, True)

## Bonus Challenge ##
# Expand on our function so that if a user is a member *and* they
# filled out a survey, they are eligible, and they get a discount.
# Then, add a `day` argument that makes anyone eligible on Fridays.

def check_eligibility(age, is_member, completed_survey, day):
    if day == 'Friday':
        print("Eligible!")
    else:
        if age < 18:
            print("Not Eligible!")
        elif is_member == True and completed_survey == True:
            print("You're eligible and you get a discount!")
        elif is_member == True or completed_survey == True:
            print("Eligible!")
        elif is_member == False and completed_survey == False:
            print("Not Eligible!")
        
# Example usage:
check_eligibility(20, True, False, 'Monday')  # "Eligible!"
check_eligibility(17, True, True, 'Sunday')   # "Not Eligible!"
check_eligibility(25, False, True, 'Wednesday')  # "Eligible!"
check_eligibility(30, False, False, 'Tuesday') # "Not Eligible!"
check_eligibility(30, True, True, 'Monday')   # "You're eligible and you get a discount!"

check_eligibility(20, True, False, 'Friday')  # "Eligible!"
check_eligibility(17, True, True, 'Friday')   # "Eligible!"
check_eligibility(25, False, True, 'Friday')  # "Eligible!"
check_eligibility(30, False, False, 'Friday') # "Eligible!"
check_eligibility(30, True, True, 'Friday')   # "Eligible!" 