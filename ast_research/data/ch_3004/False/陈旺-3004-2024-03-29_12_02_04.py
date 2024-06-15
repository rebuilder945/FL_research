a=input()
a=a.strip("[")
a=a.rstrip("]")
b=[int(i) for i in a.split(",")]
c=[]
yes=1
for i in b:
    if i==1:
       yes=0
    else:
       for x in range(2,i):
          if i%x==0:
             yes=0
if yes==1:
    c.append(i)
print(c)
        
           


