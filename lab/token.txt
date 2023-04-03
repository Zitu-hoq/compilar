keywords = {"auto","break","case","char","const","continue","default","do",
"double","else","enum","extern","float","for","goto",
"if","int","long","register","return","short","signed",
"sizeof","static","struct","switch","typedef","union",
"unsigned","void","volatile","while","printf","scanf","%d","include","stdio.h","main"}

operators = {"+","-","*","/","<",">","=","<=",">=","==","!=","++","--","%","&"}

delimiters = {'(',')','{','}','[',']','"',"'",';','#',',',''}


def detect_keywords(text):
	arr = []
	for word in text:
		if word in keywords:
			arr.append(word)
	return list(arr)


def detect_operators(text):
	arr = []
	for word in text:
		if word in operators:
			arr.append(word)
	return list(arr)


def detect_delimiters(text):
	arr = []
	for word in text:
		if word in delimiters:
			arr.append(word)
	return list(arr)


def detect_num(text):
	arr = []
	for word in text:
		try:
			a = int(word)
			arr.append(word)
		except:
			pass
	return list(arr)



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


def detect_identifiers(text):
	k = detect_keywords(text)
	o = detect_operators(text)
	d = detect_delimiters(text)
	n = detect_num(text)
	not_ident = k + o + d + n
	arr = []
	ara=[]
	for word in text:
		if word not in not_ident:
			arr.append(word)
	for word in arr:
		if(isIdentifier(word)):
			ara.append(word);
	return ara


def isString(stri):
	new = ""
	for i in range(0, len(stri)):
		if (stri[i] == '"'):
			new = stri[i]
			for j in range(i + 1, len(stri)):
				new += stri[j]
				if (stri[j] == '"'):
					ara = stri[:i]
					aString.append(new)
					arr = stri[j + 1:]
					stri = ara + arr
					return stri
	return stri




with open('example.txt') as t:
	text = t.read().split()

aString =[]


text = isString(text)
a = detect_keywords(text)
b = detect_operators(text)
c = detect_delimiters(text)
d = detect_identifiers(text)
e = detect_num(text)
print("Strings ",aString)
sum = len(a) + len(b) + len(c) + len(d) + len(e) + len(aString)

print("Keywords: ",a)
print("Operators: ",b)
print("Delimiters: ",c)
print("Identifiers: ",d)
print("Numbers: ",e)
print("total = ", sum)

