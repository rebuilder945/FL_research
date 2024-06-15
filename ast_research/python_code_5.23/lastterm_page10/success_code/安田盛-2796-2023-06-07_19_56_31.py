s=input()
a=[]
for x in range(1,len(s)):
    for i in range(len(s)-x+1):
        a.append(s[i:i+x])
a.append(s)
b=[]
x=0
for i in a:
    if i.isdigit():
        b.append(i)
        if len(i)>x:
            x=len(i)
b.reverse()
for i in b:
    if len(i)==x:
        print(i)
        break


