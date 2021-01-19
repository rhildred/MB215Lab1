def countUpperCase(sInput):
    nUpper = 0
    nLower = 0
    for sChar in sInput:
        if sChar.isupper():
            nUpper += 1
        elif sChar.islower():
            nLower += 1
    return nUpper, nLower

sUser = input("Please enter a string with both upper and lower case: ")
nUpperCase, nLowerCase = countUpperCase(sUser)
print("Your string " + sUser, "has", nUpperCase, "upper case and", nLowerCase, "lowercase.")