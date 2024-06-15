strs=eval(input)
strs=list[strs]
c=[]
if strs==[]:
    print("None")
for i in strs:
    if i not in c:
        c.append(i)
    else:
        print(i)

