#
# Sample Code for lecture on Head First Python Chapter 1
#


# To-do list
#   bash aliases / vim basics
#   Install IDLE - sudo apt-get install idle

#   Standard Library
#   List data structure
#   variable declaration / dynamic assignment
#   control structures / suites / indenting / :
#   Modulo Operator

# Get the datetime function from the datetime module
from datetime import datetime

# List of odd minutes in an hour
odds = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]

# Get the minute value from the current time
right_this_minute = datetime.today().minute

if right_this_minute in odds:
    print('This is odd!')
else:
    print('Way cool evens!')


# Run code multple times (range and its variations)
# Pause a random amount of time between executions    
