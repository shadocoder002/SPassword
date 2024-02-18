# Imports, functions/definitions, and variables

import os
import string
import sys
import time
import msvcrt as m
import subprocess as sp

schars = str(string.punctuation)
numbers = str(string.digits)
print(numbers)

def clearscreen():
    sp.call('cls' if os.name == 'nt' else 'clear', shell=True)

def halt():
    time.sleep(9999)

def presscont():
    print("Press any key to continue...")
    m.getch()
    startpage()
def passwordchecker():

    # --> Start of Configuration <--

    # If the password is in "BadWordPhrases", it will automatically flag for being to obvious
    BadWordPhrases = []

    # Min and max password lengths
    MinPasswordLength = 8
    MaxPasswordLength = 30

    # set to 0 to not check or 1 to check

    CheckSymbols = 1
    CheckNumbers = 1

    # --> End of Configuration <--

    # Entering Password to check
    Password = input("Enter Password to Check: ")

    # Checking for bad passwords below using configuration
    try:
        if Password in BadWordPhrases: print("Password contains 1 or more guessable phrases."); presscont()
        elif len(Password) < MinPasswordLength: print("Password is too short."); presscont()
        elif len(Password) > MaxPasswordLength: print("Password is too long."); presscont()
        tmp = 0
        for i in range(len(schars)):
            if schars[i] in Password: tmp = 1
        if tmp == 0 and CheckSymbols:
            print("Password doesn't have any special characters."); presscont()
        tmp = 0
        for i in range(len(numbers)):
            for x in range(len(Password)):
                if numbers[i] in Password[x]: tmp += 1
        if tmp == 0 and CheckNumbers:
            print("Password doesn't have any numbers."); presscont()
        else:
            if tmp <= 2 and CheckNumbers: print("WARNING: Password only contains 2 or less numbers.")
            print("Your password is secure!\nPress any key to continue...")
            m.getch()
            startpage()
    except: print("Something went wrong! Exception --> " + str(sys.exc_info()))

# Recommendations for secure and strong passwords
def recommend():
    print("Recommendations for a strong, secure password")
    print("1. minimum of 8 characters")
    print("2. maximum of 30-64 characters")
    print("3. limit the use of password hints")
    print("4. limit the number of failed attempts")
    print("5. use special characters (eg. !, @)")
    print("6. use capital letters and numbers")
    print("Press any key to continue...")
    m.getch()
    startpage()

# Interface user interacts with (startpage)
def startpage():
    clearscreen()
    print("1. Password Recommendations\n2. Check your password\n3. Exit")
    option = input()
    try: int(option)
    except ValueError: print("Only use numbers!")
    if option == 1:
        recommend()
    elif option == 2:
        passwordchecker()
    elif option == 3:
        quit()
    else:
        print("Invalid Option (auto clearing in 3s)"); time.sleep(3); startpage()

# Start of Program

startpage()