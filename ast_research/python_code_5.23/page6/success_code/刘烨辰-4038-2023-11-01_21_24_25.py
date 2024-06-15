n=input()
c=0
d=0
e=0
f=0
for x in n:
    if ord('a')<=ord(x)<=ord('z') or ord('A')<=ord(x)<=ord('Z'):
        c=c+1
    elif x==' ':
        d=d+1
    elif ord('0')<=ord(x)<=ord('9'):
        e=e+1
    else:
        f=f+1
print(c,d,e,f)
