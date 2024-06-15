a=0
n=0
e=0
b='1'
while b!='#':
    b=input()
    if b!='#':
        a=eval(b)
    n+=1
    e+=a
print(n-1,e-a)
