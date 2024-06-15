s = input()
alphaNum = 0
numberNum = 0
spaceNum = 0
elseNum = 0
for c in s :
    if c.isalpha():
        alphaNum += 1
    elif c.isnumeric():
        numberNum += 1
    elif c == " ":
        spaceNum += 1
    else:
        elseNum += 1
print(alphaNum,spaceNum,numberNum,elseNum)
