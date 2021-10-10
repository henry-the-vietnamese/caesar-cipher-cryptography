#!/usr/bin/env python3

#
# File:         options.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         10/10/2021
# Description:  Create functions to perform actions based on the user option.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.


def option_1(message):
    message = input('Please enter a new message: ')
    print(f'Your message is: \'{message}\'')
    return message

def option_2(OFFSET, message):
    if message == '':
        print('Error: Cannot encrypt an empty message.')
        return None
    else:
        encrypted_message = ''
        for i in message:
            encrypted_message += chr(ord(i) + OFFSET)
        print('Your message was successfully encrypted.')
        print(f'Your message is: \'{encrypted_message}\'')
        return encrypted_message
