from posixpath import split


b=[]
a=eval(input())
while a!='#':
    a.append(b)
    if a=='#':
        break
print(len(b),sum(b),split(""))
