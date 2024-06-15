strs=input()
strs=list(strs)
c=[]
if strs==[]:
    print("None")
for i in strs:
    c.append(i)
    while c[i]<=2:
        if c[i].count()==2:
            print(i)

