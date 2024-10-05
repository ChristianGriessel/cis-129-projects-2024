# Christian Griessel
# Guess the number EXTRA CREDIT for CIS 129
# A fun game for you to play

import random
import time

#runs the program
def main():
    game_logic()


def game_logic():
    #grabs random number
    number = random.randint(1, 1000)
    #iterates each attempt to change the prompt after the first attempt and print the total attempts
    i = 0
    while True:
        user_num = string_or_int_checker(i)
        #if user types Q or q the program returns 0 and breaks
        if user_num == 0:
            break
        #if user guesses correctly the program returns 1 and breaks
        reference = number_referencer(user_num, number, i)
        if reference == 1:
            break
        i += 1


def string_or_int_checker(i):
    while True:
        user_input = input_getter(i)
        #checks for sentinal value
        if user_input.lower() == "q":
            print("-----------------------------\n"
                  "YOU HAVE RETREATED IN TERROR"
                  "\n-----------------------------")
            return 0
        else:
            try:
                #gets number and forces an int
                guess = int(user_input)
                #forces a number between 1 and 1000
                if 1 <= guess <= 1000:
                    return guess
                else:
                    print('-----------------------------\n'
                          'THIS IS NOT A VALID NUMBER CAN YOU NOT READ????????'
                          '\n-----------------------------')
            #if user attempts to pass in a string this ensures the loop doesn't break
            except ValueError:
                print("-----------------------------\n"
                      "YOU MUST ENTER A NUMBER OR Q. YOU ARE NOT WORTHY OF MY GAME. NOW...AGAIN."
                      "\n-----------------------------")
                time.sleep(0.5)


def input_getter(i):
    #if it's the first attempt it provides instruction to the user
    if i == 0:
        user_input = input("GUESS A NUMBER BETWEEN 1 AND 1000 HUMAN OR TYPE 'q' TO RETREAT IN TERROR: \n")
    else:
    #subsequent attempts assume the user already knows the deal
        user_input = input("GUESS AGAIN: \n")
    return user_input


def number_referencer(user_input, number, i):
    #gets the absolute value of the difference to help user hone in on the correct number
    difference = abs(user_input - number)
    #prints different statements to help nudge the user to the correct value depending on what they guess
    if user_input > number:
        if difference <= 50:
            print("-----------------------------\n"
                  "TOO HIGH YOU'RE WITHIN 50 OF YOUR TARGET TRY HARDER"
                  "\n-----------------------------")
        elif difference <= 100:
            print("-----------------------------\n"
                  "TOO HIGH BUT YOU'RE WITHIN 100 OF YOUR TARGET"
                  "\n-----------------------------")
        elif difference <= 300:
            print("-----------------------------\n"
                  "TOO HIGH YOU'RE WITHIN 300 OF YOUR TARGET CONTINUE"
                  "\n-----------------------------")
        elif difference <= 500:
            print("-----------------------------\n"
                  "FAR TOO HIGH"
                  "\n-----------------------------")
        else:
            print("-----------------------------\n"
                  "YOU ARE NOT EVEN CLOSE PATHETIC GO MUCH LOWER"
                  "\n-----------------------------")

    elif user_input < number:
        if difference <= 50:
            print("-----------------------------\n"
                  "TOO LOW YOU'RE WITHIN 50 OF YOUR TARGET TRY HARDER"
                  "\n-----------------------------")
        elif difference <= 100:
            print("-----------------------------\n"
                  "TOO LOW BUT YOU'RE WITHIN 100 OF YOUR TARGET"
                  "\n-----------------------------")
        elif difference <= 300:
            print("-----------------------------\n"
                  "TOO LOW BUT YOU'RE WITHIN 300 OF YOUR TARGET CONTINUE"
                  "\n-----------------------------")
        elif difference <= 500:
            print("-----------------------------\n"
                  "FAR TOO LOW"
                  "\n-----------------------------")
        else:
            print("-----------------------------\n"
                  "AIM HIGHER FLESHSACK"
                  "\n-----------------------------")

    else:
        #prints a success message as well as the number of attempts it took to get the correct int
        print("-----------------------------\n"
              "THIS IS YOUR NUMBER. WHAT A FUN GAME IT HAS BEEN. CONGRATULATIONS. PREPARE TO BE DESTROYED"
              f" IT TOOK YOU {i + 1} PATHETIC GUESSES"
              "\n-----------------------------")
        return 1


main()
