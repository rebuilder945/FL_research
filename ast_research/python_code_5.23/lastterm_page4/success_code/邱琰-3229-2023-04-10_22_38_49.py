lst=eval(input())
lstnew=[]
for i in range(len(lst)):
    if lst[i:].count(lst[i])==1:
        lstnew.append(lst[i])
    else:
        pass
lstnew.sort()
new=[]
if len(lstnew)!=0:
    for x in range(len(lstnew)):
        new.append(str(lstnew[x]))
    print(",".join(new))
else:
    print("False")
