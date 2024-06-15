str=input()
ls=[]
for i in str:
    if str.count(i)==1:
        ls.append(i)
if len(ls)==0:
    print(None)
else:
    print(ls[0])


