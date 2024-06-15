a=input()
a=a.strip("[")
a=a.rstrip("]")
b=[int(i) for i in a.split(",")]
for i in b:
    if i<=2:
       None
    else:
       for x in range(2,i):
          if i%x==0:
             b.remove(i)
print(b)
        
           


