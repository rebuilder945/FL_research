from posixpath import split


b=[]
while a!='#':
    a=eval(input())
    a.append(b)
    if a=='#':
        break
print(len(b),sum(b),split(""))
