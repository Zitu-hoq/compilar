
def isString(stri):
	for i in range(0, len(stri)):
		if (stri[i] == '"'):
			for j in range(i + 1, len(stri)):
				if (stri[j] == '"'):
					ara = stri[:i]
					arr = stri[j + 1:]
					stri = ara + arr
					return stri
	return stri


with open('example.txt') as t:
	text = t.read().split()


text = isString(text)
print(text)