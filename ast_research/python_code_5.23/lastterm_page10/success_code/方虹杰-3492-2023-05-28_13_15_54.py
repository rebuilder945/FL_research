a=input()
b=list(a)
c=[]
if a=="":
    print("None")
else:
    for i in b:
        if b.count(i)==1:
            c.append(i)
        
    print(c[0])
    

