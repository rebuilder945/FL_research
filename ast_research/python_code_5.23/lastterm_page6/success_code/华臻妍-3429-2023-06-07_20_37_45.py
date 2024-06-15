tmpStr=input()
alphaNum=0
numbers=0
spaceNum=0
otherNum=0
for i in tmpStr:
    if i.isalpha():
        alphaNum+=1
    elif i.isnumeric():
        numbers+=1
    elif i.isspace():
        spaceNum+=1
    else:
        otherNum+=1
print(alphaNum,spaceNum,numbers,otherNum)
    
