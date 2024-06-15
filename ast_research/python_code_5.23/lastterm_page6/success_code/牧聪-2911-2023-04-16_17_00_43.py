a=input("")
a=a.split()
b=[]
for x in a:
    x=int((x+5)%10)
    b.append(x)
b.reverse()
b="".join(str(i) for i in b)

