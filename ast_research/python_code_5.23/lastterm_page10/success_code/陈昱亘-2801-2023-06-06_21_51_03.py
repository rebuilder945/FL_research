password=input()
intensity=0
a,b,c,d,e=0,0,0,0,0
if len(password)>=8:
    a=1
for x in password:
    if x.isdigit():
        b=1
    if x.islower():
        c=1
    if x.isupper():
        d=1
    if x in ['~','!','@','#','$','%','^','&','*','()','_','=','-','/','.','?','<','>',';',':','[',']','{','}','\\','|']:
        e=1
intensity=a+b+c+d+e
print(intensity)
