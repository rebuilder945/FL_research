lst=eval(input())
lst.reverse()
prt=[]
for i in lst:
    if i not in prt:
        prt.append(i)
prt.reverse()
print(prt)
    
