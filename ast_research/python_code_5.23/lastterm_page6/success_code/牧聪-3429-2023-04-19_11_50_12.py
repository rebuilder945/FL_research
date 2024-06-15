hobby=str(input())
lst=list(hobby)
letter=0
num=0
other=0
speace=0
for x in lst:
    if x in [chr(i)for i in range(97,123) and range(65,91)]:
        letter+=1
    elif x==" ":
        speace+=1
    elif x not in [str(q) for q in range(10)]:
        other+=1
    else:
        num+=1        
print(letter,speace,num,other)
        


