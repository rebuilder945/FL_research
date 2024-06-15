n=input()
a=0
ls=['~','!','@','#','$','%','^','&','*','(',')','_','=','-','/',',','.','?','<','>',';',':','||','\\','{','}','[',']']
if len(n)>=8:
    a+=1
for i in n:
    while i.isnumeric():
        a+=1
        break
    while i.islower():
        a+=1
        break
    while i.isupper():
        a+=1
        break
    while i in ls:
        a+=1
print(a)
