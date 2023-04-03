
def isComment(line):
    if (line[0] == '/' and line[1] == '/' and line[2] != '/'):
        print("It is a single-line comment")
        return

    if (line[len(line) - 2] == '*' and line[len(line) - 1] == '/' and line[0] == '/' and line[1] == '*'):
        print("It is a multi-line comment")
        return

    print("It is not a comment")


while(True):
    line = input("(For exit type 0) Enter Your Text: ")
    if(line == '0'):
        break
    else:
        isComment(line)

