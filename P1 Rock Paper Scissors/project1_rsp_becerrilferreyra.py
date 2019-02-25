# project1_rps_becerrilferreyra.py
#
# Name(s): Rodrigo Becerril Ferreyra
#
# Date: 2019-02-25
#
#
import random #for random choice of bot

# RPS is all the possible choices
RPS = ["R", "P", "S"]

while True:
    # getting and parsing user input
    user_choice = input("\nPlease enter your choice of \"(R)ock\", \"(P)aper\", or \"(S)cissors\".\n")
    # input gets stripped down to first character
    user_choice = user_choice[0]
    user_choice = user_choice.upper()
    
    # input validation
    # will infini-loop if user does not have the correct input
    if (user_choice != RPS[0]) and (user_choice != RPS[1]) and (user_choice != RPS[2]):
        print("Input is invalid. Please re-enter your input.")
        continue

    # logic goes here

    break
print("Input correct")
