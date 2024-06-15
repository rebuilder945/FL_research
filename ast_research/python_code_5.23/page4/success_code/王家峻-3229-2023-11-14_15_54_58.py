n=eval(input())
c=[]
for x in n:
    if n.count(x)==1:
        c.append(x)
        print(c)      
    else:
        print(False)
  

