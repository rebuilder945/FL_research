strs=input()
strs=list(strs)
c=[]
if strs==[]:
    print("None")
for i in strs:
    c.append(i)
    if strs.count(i) == 1:
        print(i)
        break

