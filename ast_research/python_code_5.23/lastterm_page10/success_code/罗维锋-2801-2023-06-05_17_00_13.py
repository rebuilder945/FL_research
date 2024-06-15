a=input()
b=list(map(str,list(range(10))))
c=list(map(chr,list(range(97,123))))
d=list(map(chr,list(range(65,91))))
e=len(a)
s=0
f=['~','!','@','#','$','%','^','&','*','(',')','_','=','-','/'',','.','?','<','>',';',':','[',']','{','}','|','\\']
for x in a:
    if x in b:
        s+=1
        break
for x in a:
    if x in c:
        s+=1
        break
for x in a:
    if x in d:
        s+=1
        break
for x in a:
    if x in f:
        s+=1
        break
if e>=8:
    s+=1
print(s)
