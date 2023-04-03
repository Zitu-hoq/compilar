
def isIdentifier(word):
    letter = list(word)
    if(((ord(letter[0]) >= ord('A') and ord(letter[0]) <= ord('Z')) or
             (ord(letter[0]) <= ord('z') and ord(letter[0]) >= ord('a')) or
             (ord(letter[0]) == ord('_'))) == False):
        return False

    for i in range(1,len(letter)):
        if (((ord(letter[i]) >= ord('A') and ord(letter[i]) <= ord('Z')) or
             (ord(letter[i]) <= ord('z') and ord(letter[i]) >= ord('a')) or
             (ord(letter[i]) == ord('_')) or
             (ord(letter[i]) >= ord('0') and ord(letter[i]) <= ord('9'))) == False):
            return False

    return True


def isKeyword(word):
    keyword = ['auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do',
               'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if',
               'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static',
               'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while']
    for j in keyword:
        if(j == word):
            print(j, ' is a keyword')
            return

    if(isIdentifier(word)):
        print(word, "is a valid Identifier")
    else:
        print(word, "is invalide")


def isChecker(text):
    word = text.split()
    for i in word:
        isKeyword(i)


text_input = input("Enter your Text : ")
isChecker(text_input)
