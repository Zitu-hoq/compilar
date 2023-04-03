def isExponential(word):
    letter = list(word)
    for i in range(0,len(letter)):
        if(letter[0] == "e"):
            return False
        elif(letter[i] == "e"):
            if((i+1) != len(letter)):
                return True
            else:
                return False


def isInt(word):
    try:
        int(word)
        return True
    except:
        return False


def isFloat(word):
    try:
        float(word)
        return True
    except:
        return False


def isNumber(word):

    if(isInt(word)):
        print(word + " is an integer")
    elif(isExponential(word)):
        print(word+ " is an Expoentioal")
    elif (isFloat(word)):
        print(word + " is a float")
    else:
        print(word + " is not a number")


while(True):
    line = input("(For exit type 0) Enter a number: ")
    if(line == "0"):
        break
    else:
        word = line.split()
        for i in word:
            isNumber(i)

