ls=eval(input())
ls1=[]
for i in range(len(ls)):
    if ls.count(ls[i])==1:
        ls1.append(ls[i]) 
        ls1.sort()
if ls1!=[]:
    print(','.join(map(str,ls1)))
else:
    print(False)

