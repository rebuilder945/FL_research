a=input()
n=0
b='0123456789'
c='abcdefghijklmnopqrstuvwxyz'
d='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
e='~!@#$%^&*()_=-/,.?<>;:[]{\}\|\\'
for i in a:
    if i in b:
        n+=1
        break
for i in a:
    if i in c:
        n+=1
        break
for i in a:
    if i in d:
        n+=1
        break
if len(a)>=8:
    n+=1
for i in a:
    if i in e:
        n+=1
        break
print(n)
