lst=eval(input())
nl=[]
for i in lst:
    if i!=0:
        nl.append(i)
for i in lst:
    if i==0:
        nl.append(i)
print(nl)

