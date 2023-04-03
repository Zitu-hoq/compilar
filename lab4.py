
from itertools import takewhile


def leftFactor(s, alphabet):


    def groupby(ls):
        d = {}
        ls = [y[0] for y in rules]
        initial = list(set(ls))
        for y in initial:
            for i in rules:
                if i.startswith(y):
                    if y not in d:
                        d[y] = []
                    d[y].append(i)
        return d

    def prefix(x):
        return len(set(x)) == 1

    starting = ""
    rules = []
    common = []
    s = s.replace(" ", "").replace("	", "").replace("\n", "")

    while (True):
        rules = []
        common = []
        split = s.split("->")
        starting = split[0]
        for i in split[1].split("|"):
            rules.append(i)

        # logic for taking commons out
        for k, l in groupby(rules).items():
            r = [l[0] for l in takewhile(prefix, zip(*l))]
            common.append(''.join(r))
        # end of taking commons
        for i in common:
            newalphabet = alphabet
            print(starting + "->" + i + newalphabet)
            index = []
            for k in rules:
                if (k.startswith(i)):
                    index.append(k)
            print(newalphabet + "->", end="")
            for j in index[:-1]:
                stringtoprint = j.replace(i, "", 1) + "|"
                if stringtoprint == "|":
                    print("\u03B5", "|", end="")
                else:
                    print(j.replace(i, "", 1) + "|", end="")
            stringtoprint = index[-1].replace(i, "", 1) + "|"
            if stringtoprint == "|":
                print("\u03B5", "", end="")
            else:
                print(index[-1].replace(i, "", 1) + "", end="")
            print("")
        rules.clear()
        common.clear()
        break

# S->iEtS|iEtSes|a

num = int(input("Number of production rule "))
ara = []
for i in range(0, num):
    txt = input("Enter you production rules ")
    ara.append(txt)


for i in ara:
    split = i.split("->")
    start = split[0] + "'"

    leftFactor(i, start)

