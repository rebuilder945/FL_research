c=input()
a=0
for i in c:
    if "0"<=i<="9":
        a+=1
        break
for i in c:
    if "a"<=i<="z":
        a+=1
        break
for i in c:
    if "A"<=i<="Z":
        a+=1
        break
if len(c)>=8:
    a+=1
d=['~','!','@','#','$','%','^','&','*','(',')','_','=','-','/','.','?','<',',','>',';',':','[',']','{','}','|',"\\"]
for i in c:
    if i in d:
        a+=1
        break
print(a)




