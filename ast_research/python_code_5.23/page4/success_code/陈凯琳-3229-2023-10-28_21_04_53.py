a=eval(input())
lit=list(set(a))
lit1=[]
for i in range(len(lit)):
    if a.count(lit[i])==1:
        lit1.append(str(lit[i]))
lit1.sort()
if len(lit1)==0:
    print('False')
else:
    print(','.join(lit1))




