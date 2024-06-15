a=input()
b=[]
for i in a:
    b.append(i)
c=[]
for i in b:
    d=eval(i)
    e=(d+5)%10
    c.append(e)
c.reverse()
print("".join(map(str,c)))
