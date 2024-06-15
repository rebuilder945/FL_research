strs=input()
strs=list(strs)
c=[]
if strs==[]:
    print("None")
for i in strs:
    c.append(i)
    if i.count()==2:
        print(i)
    break

