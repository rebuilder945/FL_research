n=input()
a=0
b=0
c=0
d=0
e=0
ls=['~','!','@','#','$','%','^','&','*','(',')','_','=','-','/',',','.','?','<','>',';',':','||','\\','{','}','[',']']
if len(n)>=8:
    a=1
for i in n:
    if i.isnumeric():
        b=1
    if i.islower():
        c=1
    if i.isupper():
        d=1
    if i in ls:
        e=1
print(a+b+c+d+e)
