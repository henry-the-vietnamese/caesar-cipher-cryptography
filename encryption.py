#!/usr/bin/env python3

#
# File:         encryption.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         10/10/2021
# Description:  Use Caesar Cipher technique to encrypt or decrypt an inputted message.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.


# Menu Driven Program:
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

option = int(input('Enter an option (1,2,3,4): '))

# Input Validation.
while option not in range(1, 5):
    option = int(input('Invalid choice. Enter an option (1,2,3,4): '))

# Now we have a valid option.
if option == 1:
    print('Option 1: Enter Message')
elif option == 2:
    print('Option 2: Encrypt Message')
elif option == 3:
    print('Option 3: Decrypt Message')
else:
    print('\nGoodbye')



