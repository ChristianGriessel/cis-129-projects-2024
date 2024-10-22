# Author: Christian Griessel
# Student Pass Fail program
# Takes a 1 or 2 depending on whether a student passed or failed
# Uses a flag to decide whether a valid input has been given. If not it reprompts.
"""Using nested control statements to analyze examination results."""

# initialize variables
passes = 0  # number of passes
failures = 0  # number of failures

NMB_OF_STUDENTS = 10  # process 10 students
for student in range(NMB_OF_STUDENTS):
    valid_input = False
    while not valid_input:
        result = input('Enter result (1=pass, 2=fail): ')
        if result == '1' and int(result) == 1:
            passes = passes + 1
            valid_input = True
        elif result == '2' and int(result) == 2:
            failures = failures + 1
            valid_input = True
        else:
            print("NOT A VALID VALUE")

# termination phase
print('Passed:', passes)
print('Failed:', failures)

if passes > 8:
    print('Bonus to instructor')