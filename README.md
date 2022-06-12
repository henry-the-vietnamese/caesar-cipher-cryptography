# Table of Contents

1. [Aim](#aim)
1. [Introduction](#introduction)
1. [Mainly Used Functions](#mainly-used-functions)
1. [Options](#options)
1. [Encryption Process](#encryption-process)
1. [Decryption Process](#decryption-process)
1. [Sample Output](https://github.com/tanducmai/caesar-cipher-cryptography/blob/main/sample_output.pdf)

# Aim

Use Caesar Cipher technique to encrypt or decrypt an inputted message.

# Introduction

A simple way to encrypt data is attributed to [Julius
Caesar](http://en.wikipedia.org/wiki/Caesar_cipher), the Roman Emperor. This
method takes each character in a message and replaces it with one which is a
certain distance (offset) along the alphabet from it.

For example:
![Exaxmple of the technique](assets/example.png)

If the offset is 3 then A becomes D, B becomes E, C becomes F etc.

Encrypting DIG with the offset of +3 will result in GLJ. The decrypt GLJ, simply
offset by the same amount in the opposite direction (i.e. with the negative
offset -3).

Instead of restricting the cipher to the alphabetic characters only, we will use
all the printable ASCII characters. That is, all the characters from ASCII 32
(Space) to ASCII 126 (~).

# Mainly used functions

1. **ord(c)**


   If *c* is a string of length 1, *ord(c)* returns an integer representing the
   ASCII value of the string.

   For example: *ord(*'*a*'*)* returns the integer *97*.

2. **chr(i)**

   If *i* is an integer, *chr(i)* returns a string containing only one character
   with an ASCII code is equal to the integer *i*.

   For example: *chr(97)* returns the string '*a*'

# Options

Includes many functions that collectively simulate a menu driven program that
will allow the user to enter commands and process these commands until the quit
command is entered.

The following commands should be allowed:
1. **Enter Message**:

   Prompt for and read (from the keyboard) a string to be encrypted.

2. **Encrypt Message**:

   Encrypts the previously entered message or displays an error message if no
   string was entered. The message will be encrypted using a randomly generated
   number between 32 and 126 as the offset/encryption key.  This encryption key
   will be converted into a character using *chr(i)* and appended to the
   encrypted string.

3. **Decrypt Message**:

   Decrypts the previously entered message or displays an error message if no
   string was entered. The message will be decrypted by converting the last
   letter in the string (the encryption key) to its ASCII value, and using this
   to offset all other characters in the negative direction. The encryption key
   should then be removed from the message.

4. **Quit**:

   Displays a goodbye message to the screen and quits the program.

# Encryption Process

To start with, choose 1 as the offset. In this case, if the message 'abG' is
enterered, after the encryption, the result should be 'bcH'. Now that it is
working, use the *randint()* function from the *random* module to make the
offset a random number between 32 and 126.

![Printable ASCII character set](assets/printable-ascii.png)

The program only work with the printable ASCII character set. That is, all the
characters from ASCII 32 (Space) to ASCII 126 (~). When the ASCII value of the
encrypted character points to a character beyond 126 it should *wrap* around to
the beginning of the set.

For example, if the offset is 4 and the character is '}' (ASCII 125) then it
will encrypt to ASCII 129. This is beyond 126 so you should subtract the total
number of characters in the set (95) to wrap back to the beginning. The
resulting encrypted character will be the double-quote character " (129-95,
ASCII 34). You may have to subtract 95 multiple times until it is within the
set, for example, '}' + '}' is 250, and minus 95 is 155. This is still out of
bounds. Use a loop. Note that if the encrypted string contains characters that
are not in the table above, then your ASCII values are not 'wrapping' correctly.

# Decryption Process

The encryption key will be found as the last character in the string.  Subtract
this offset from the ASCII value of each other character in the message
variable. These ASCII values will then need to be converted back to characters
using the chr(i) function.

Again, the program only work with the printable ASCII character set. That is,
all the characters from ASCII 32 (Space) to ASCII 126 (~). When the offset
points to a character less than 32 it should *wrap* around to the end of the
set.

For example, if the offset is 4 and the character is '!' (ASCII 33) then it will
decrypt to ASCII 29. This is less than 32 so wrap back to the end by adding the
total number of characters (95). This gives character '|' (29+95, ASCII 124).
You may have to add 95 multiple times until it is within the set. Use a loop.

# Sample Output

```text
-------------------
     MAIN MENU
-------------------
1. Enter Message
2. Encrypt Message
3. Decrypt Message
4. Quit

Enter an option (1,2,3,4): 1
Please enter a new message: The rabbit has sprung.
Your message is: 'The rabbit has sprung.'.

-------------------
     MAIN MENU
-------------------
1. Enter Message
2. Encrypt Message
3. Decrypt Message
4. Quit

Enter an option (1,2,3,4): 2
Your message was successfully encrypted.
Your message is: '`tq,~mnnu!,tm , |~"zs:k'.

-------------------
     MAIN MENU
-------------------
1. Enter Message
2. Encrypt Message
3. Decrypt Message
4. Quit

Enter an option (1,2,3,4): 1
Please enter a new message: The conference will commence.
Your message is: 'The conference will commence.'.

-------------------
     MAIN MENU
-------------------
1. Enter Message
2. Encrypt Message
3. Decrypt Message
4. Quit

Enter an option (1,2,3,4): 3
Your message was successfully decrypted.
Your message is: '&:7Q5A@87D7@57QI;>>Q5A??7@57'.

-------------------
     MAIN MENU
-------------------
1. Enter Message
2. Encrypt Message
3. Decrypt Message
4. Quit

Enter an option (1,2,3,4): 2
Your message was successfully encrypted.
Your message is: 'BVSmQ]\TS`S\QSmeWZZmQ][[S\QS{'.

-------------------
     MAIN MENU
-------------------
1. Enter Message
2. Encrypt Message
3. Decrypt Message
4. Quit

Enter an option (1,2,3,4): 4
Your message is: 'BVSmQ]\TS`S\QSmeWZZmQ][[S\QS{'.

Goodbye
```
