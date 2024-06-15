a=0
c=0
e=0
b='1'
while b!='#':
    b=input()
    if b!='#':
        a=eval(b)
    c+=1
    e+=a
print("{} {}".format(c-1,e-a))
