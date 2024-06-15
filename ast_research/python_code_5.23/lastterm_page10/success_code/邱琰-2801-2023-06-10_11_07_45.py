n=list(input())
a,b,c,d,e=0,0,0,0,0
if len(n)>=8:
    a=1
for i in n:
    if i.islower():
        b=1
    if i.upper():
        c=1
    if i.isdigit():
        d=1
    if i in ['~','!','@','#','$','%','^','&','*','(',')','_','=','-','/',',','.','?','<','>',';',':','[',']','{','}','|','\\']:
        e=1
print(a+b+c+d+e)
