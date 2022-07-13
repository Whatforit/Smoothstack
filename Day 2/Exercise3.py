print("Hello world"[8])
# r

print("thinker"[2:5])
# ink

s = "Sammy"
print(s[2:])
# mmy

print(set("Mississippi"))
# {'M', 'i', 's', 'p'}


punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
i = int(input())
checkList = []
while(i > 0):
    word = input().replace(" ", "").lower()
    for c in word:
        if c in punc:
            word = word.replace(c, "")
    pal = word.replace(" ", "").lower()[::-1]
    if(word == pal):
        checkList.append("Y")
    else:
        checkList.append("N")
    i -= 1
for i in checkList:
    print(i + " ", end="")




