n=input() or '#'
a=0
b=0
while(n!='#'):
    a+=int(n)
    b+=1
    n=input() or '#'
print(b,end=' ')
print(a,end=' ')


