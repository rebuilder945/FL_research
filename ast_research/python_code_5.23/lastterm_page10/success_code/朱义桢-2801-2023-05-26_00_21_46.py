a=input()
b=map(str,list(x for x in range(0,10)))
c=['~','!','@','#','$','%','^','&','*','(',')','_','=','-','/',',','.','?','<','>',';',':','[',']','{','}','|','\'']
m=0
while len(a)>=8:
    m+=1
    break
a=" ".join(a)
a=a.split()
for x in a:
    if x in b:
        m+=1
        break
for x in a:
    if "a"<=x<="z":
        m+=1
        break
for x in a:
    if "A"<=x<="Z":
        m+=1
        break
for x in a:
    if x in c:
        m+=1
        break
print(m)
