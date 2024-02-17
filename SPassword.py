# Imports and functions/definitions

import os
import time
import msvcrt as m
import subprocess as sp

def clearscreen():
    sp.call('cls' if os.name == 'nt' else 'clear', shell=True)

def halt():
    time.sleep(9999)

def presscont():
    print("Press any key to continue...")
    m.getch()
def passwordchecker():

    # --> Start of Configuration <--

    # My default complies with NIST standards
    # Any words included in "BadWordPhrases" will automatically flag for being to obvious
    BadWordPhrases = ["password", "secret", "1234", "a"]

    # Min and max password lengths
    MinPasswordLength = 8
    MaxPasswordLength = 30

    # --> End of Configuration <--

    # Entering Password to check
    Password = input("Enter Password to Check: ")

    # Checking for bad passwords using configuration below

    if Password in BadWordPhrases: print("Password contains 1 or more guessable phrases."); presscont()
    elif len(Password) < MinPasswordLength: print("Password is too short."); presscont()
    elif len(Password) > MaxPasswordLength: print("Password is too long."); presscont()
    else:
        print("Your password is secure!\n Press any key to continue...")
        m.getch()


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
    option = int(input())
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