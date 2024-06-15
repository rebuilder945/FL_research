a=input()
b=list(a)
c=[]
if a=="":
    print("None")
elif a!="":
    for i in range(len(b)):
        if b.count(b[i])==1:
            c.append(b[i])
    print(c[0])




