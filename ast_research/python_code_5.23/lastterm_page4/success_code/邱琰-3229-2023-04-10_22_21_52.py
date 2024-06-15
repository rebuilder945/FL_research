lst=eval(input())
lstnew=[]
for i in range(len(lst)):
    if lst[i:].count(lst[i])==1:
        lstnew.append(lst[i])
if lstnew==[]:
    print(False)
else:
    print(','.join(lstnew.sort()))
