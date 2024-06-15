a=eval(input())
b=''
while len(a)>0:
    c=max(a)
    b+=str(c)
    a.remove(c)
print(b)
