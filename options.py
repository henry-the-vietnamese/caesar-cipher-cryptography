#!/usr/bin/env python3

#
# File:         options.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         10-Oct-2021
# Description:  Create functions to display the menu driven program, validate
#               user option, and perform actions based on the user option.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.


# ------------------------------- Module Import -------------------------------
"""
The random module helps randomise the offset value, hence unpredictable
encryption.
"""
import random


# ---------------------------- Function Definitions ---------------------------
def menu_driven_program():
    print(
    """
-------------------
     MAIN MENU
-------------------
1. Enter Message
2. Encrypt Message
3. Decrypt Message
4. Quit
"""
    )


def validate_option():
    """
    Function to validate the user choice. Creating this function allows the
    validation (using try/except/finally) to continuously repeats until a valid
    option is made.
    This function tales no parameters, as well as no global variables.
    Returns: the finally valid guess is returned.
    """
    try:
        option = int(input('Enter an option (1,2,3,4): '))
    except ValueError:
        print('Invalid choice. It should be an integer data type.')
        option = validate_option()
    finally:
        while option not in range(1, 5):
            option = int(input('Invalid choice. Enter an option (1,2,3,4): '))
        return option


def option_1(message):
    """
    Function to prompt for and display the user message to the screen.
    This function takes one parameter which is the empty message variable
    created initially.
    Parameters: message.
    Returns: the message that the user inputted is returned from the function.
    """
    message = input('Please enter a new message: ')
    if message != '':
        print(f'Your message is: \'{message}\'.')
    return message


def option_2(message):
    """
    Function to encrypt the message inputted by the user (no encryption happens
    if the message is empty).
    This function takes one parameter which is the message inputted previously
    in command 1.
    Parameters: message.
    Returns: the message that has been successfully encrypted is returned from
    the function.
    """
    if message == '':
        print('Error: Cannot encrypt an empty message.')
        return ''
    else:
        OFFSET = random.randint(32, 126)
        encrypted_message = ''
        for i in message:
            UNICODE_VALUE = ord(i) + OFFSET
            while UNICODE_VALUE > 126:
                UNICODE_VALUE -= 95
            encrypted_message += chr(UNICODE_VALUE)
        encrypted_message += chr(OFFSET)
        print('Your message was successfully encrypted.')
        print(f'Your message is: \'{encrypted_message}\'.')
        return encrypted_message


def option_3(encrypted_message):
    """
    Function to decrypt the the message that has been encrypted (no encryption
    happens if the message is empty).
    This function takes one parameter which is the message inputted previously
    in command 1 and then encrypted using command 2.
    Parameters: encrypted_message.
    Returns: the message that has been successfully decrypted is returned from
    the function.
    """
    if encrypted_message == '':
        print('Error: Cannot decrypt an empty message.')
        return ''
    else:
        OFFSET = ord(encrypted_message[-1])
        decrypted_message = ''
        for i in encrypted_message:
            UNICODE_VALUE = ord(i) - OFFSET
            while UNICODE_VALUE < 32:
                UNICODE_VALUE += 95
            decrypted_message += chr(UNICODE_VALUE)
        print('Your message was successfully decrypted.')
        print(f'Your message is: \'{decrypted_message[:-1]}\'.')
        return decrypted_message[:-1]
