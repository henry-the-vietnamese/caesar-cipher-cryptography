#!/usr/bin/python3

#
# File:         main.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         10-Oct-2021
# Description:  Use Caesar Cipher technique to encrypt or decrypt an
#               inputted message.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.


# ------------------------------- Module Import -------------------------------
"""
The predefined options module consists of three functions that take place as
soon as the user inputs an option - which is also evaluated using another
function.
Another function in the options module is the one that displays the
menu driven program, which is helpful since the menu is repeatedly used in the
main program.
"""
import options


# ---------------------------------- Program ----------------------------------
if __name__ == '__main__':
    options.menu_driven_program()
    message = ''

    # Input Validation
    option = options.ValidOption()

    # Now we have a valid option.
    while option != 4:
        if option == 1:
            message = options.option_1(message)
        elif option == 2:
            message = options.option_2(message)
        else:
            message = options.option_3(message)
        options.menu_driven_program()
        option = options.ValidOption()

    #Exit the loop, meaning option == 4:
    if message != '':
        print(f'Your message is: \'{message}\'.')
    print('\nGoodbye')
