a=eval(input())
lit=[]
for i in range(len(a)):
    if a.count(i)==1:
        lit.append(i)
lit.sort()
if len(lit)==0:
    print(False)
else:
    print(lit)




