


def isOperator(oprtr):
    operators = ['+ Addition', '- Subtraction', '* Multiplication', '% Reminder', '/ Division',
                 '++ Increment', '-- Decrement', '&& Logical-And', '== Equal-To', '= Assignment',
                 '!= Not-Equal', '> Grater-Than', '< Less-Than', '<= Less-Than-Equal', '>= Greater-Than-Equal',
                 '|| Logical-OR', '! Logical-Not', '& Bitwise-And', '| Bitwise-OR', '^ Bitwise-Exclusive-OR',
                 '<< Shift-Left', '>> Shift-Right', '~ Bitwise-Complement', '<> Not-Equal']
    for i in operators:
        value = i.split()
        if(oprtr == value[0]):
            print("'", value[0], "' is ", value[1], " operator")
            return
    print(oprtr, "is not an operator")


print("Enter 0 to Exit")
while(True):
    line = input("Enter your operator: ")
    if(line == '0'):
        break
    else:
        word = line.split()
        for i in word:
            isOperator(i)