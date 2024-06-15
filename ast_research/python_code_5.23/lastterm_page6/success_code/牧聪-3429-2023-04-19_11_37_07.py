hobby=str(input())
lst=list(hobby)
letter=0
num=0
other=0
speace=0
for x in lst:
    if int(x) in range(10):
        num+=1
    elif eval(x) in [chr(i)for i in range(97,123)]:
        letter+=1
    elif x==" ":
        speace+=1
    else:
        other+=1
print(letter,speace,num,other)
