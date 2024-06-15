str=input()
ls=[]
for s in str:
    if str.count(s)==1:
        ls.append(s)
print(ls[0])
