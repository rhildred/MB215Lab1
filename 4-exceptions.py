try:
    nGrade = int(input("please enter your grade"))
    if nGrade < 50:
        print("you failed")
    elif nGrade >= 90:
        print("A+")
    else:
        print("you passed")
except:
    print("please enter a grade between 0 and 100")
