a=input()
a=a.strip("[")
a=a.rstrip("]")
b=[int(i) for i in a.split(",")]
c=sorted(b)
for x in range(int(b.count(c[0]))):
     if c[0] in b:
        b.remove(c[0])
if len(b)==0:
   print(b)
elif len(b)>=1: 
    for x in range(int(b.count(c[-1]))): 
        b.remove(c[-1])
    print(b)



