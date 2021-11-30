import string
import re

print(f"\tWelcome to Password Validator, type your desired password and we'll check them for you!")

# function for checking the characters
def checker(passF):

    # arranging the COUNT VARIABLES and setting the first value to 0
    validCount = 0
    upperletterValidCount = 0
    lowerletterValidCount = 0
    numberValidCount = 0
    specCharValidCount = 0
    spaceValidCount = 0

    # arranging the VARIABLES and listing their value (in string)
    upperletters = string.ascii_uppercase
    lowerletters = string.ascii_lowercase
    numbers = re.split(r"\s", "0 1 2 3 4 5 6 7 8 9")
    specChar = re.split(r"\s", "! @ # $ % ^ & * ( ) - _ = + [ ] { } \ | ; : , < . > / ? ~")
    space = [" "]

    # checking if the password met the minimum number of characters
    length = len(passF)
    if length >= 15:
        validCount = validCount + 1
    else:
        validCount = validCount + 0

    # arranging the conditions by space > uppercase > lowercase > numbers > special characters
    for p in passF:
        if p in space:
            spaceValidCount = spaceValidCount + 1
        else: 
            spaceValidCount = spaceValidCount + 0
            if p in upperletters:
                upperletterValidCount = upperletterValidCount + 1
            else:
                upperletterValidCount = upperletterValidCount + 0
                if p in lowerletters:
                    lowerletterValidCount = lowerletterValidCount + 1
                else:
                    lowerletterValidCount = lowerletterValidCount + 0
                    if p in numbers:
                        numberValidCount = numberValidCount + 1
                    else:
                        numberValidCount = numberValidCount + 0
                        if p in specChar:
                            specCharValidCount = specCharValidCount + 1
                        else:
                            specCharValidCount = specCharValidCount + 0

    # checking the validCount of each variables
    if upperletterValidCount >= 1:
        validCount = validCount + 1
    else:
        validCount = validCount + 0

    if lowerletterValidCount >= 1:
        validCount = validCount + 1
    else:
        validCount = validCount + 0

    if numberValidCount >= 1:
        validCount = validCount + 1
    else:
        validCount = validCount + 0

    if specCharValidCount >= 1:
        validCount = validCount + 1
    else:
        validCount = validCount + 0

    if spaceValidCount < 1:
        validCount = validCount + 1
    else:
        validCount = validCount + 0

    # making the conditions for validCount
    if validCount < 6:
        print("Invalid, please try again.")
    else:
        print("Valid, your password is good to go.")

# asking for the input
print(f"REQUIREMENTS:\n- minimum of 15 characters\n- strictly no space\n- at least ONE uppercase letter\n- at least ONE lowercase letter\n- at least ONE number\n- at least ONE special character")
password = input("Password: ")

# calling the function with the password variable to be checked
checker(password)