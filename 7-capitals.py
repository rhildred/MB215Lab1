dictCapitals = {"ON":"Toronto","MB":"Winnipeg","BC":"Victoria"}

def getCapital(sProv):
    global dictCapitals
    return dictCapitals[sProv]

try:
    sAbbreviation = input("Enter a short form for a province: ")
    sCapital = getCapital(sAbbreviation)
    print("The capital of", sAbbreviation, "is", sCapital)
except:
    # there is a lot going on here!
    print("Please enter a province from", list(dictCapitals.keys()))