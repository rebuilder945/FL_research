a=input()
a=a.strip("[")
a=a.rstrip("]")
b=[int(i) for i in a.split(",")]
c=[]
for i in b:
    for x in range(2,i):
        if i%x==0:
           c.append(i)
print(c)
        
           


