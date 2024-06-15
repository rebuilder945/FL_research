n=input()
a=0
ls=['~','!','@','#','$','%','^','&','*','(',')','_','=','-','/',',','.','?','<','>',';',':','||','\\','{','}','[',']']
if len(n)>=8:
    a+=1
for i in n:
    if i.isnumeric():
        a+=1
        break
    if i.islower():
        a+=1
        break
    if i.isupper():
        a+=1
        break
    if i in ls:
        a+=1
        break
print(a)
