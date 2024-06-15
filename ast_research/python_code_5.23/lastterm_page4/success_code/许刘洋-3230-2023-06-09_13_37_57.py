a=eval(input())
b=''
while len(a)>0:
    c=max(a)
    b+=c
    a.remove(c)
print(b)
