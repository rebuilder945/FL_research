from posixpath import split


b=[]
a=eval(input())
while a!='#':
    b.append(a)
    if a=='#':
        break
print(len(b),sum(b),split(""))
