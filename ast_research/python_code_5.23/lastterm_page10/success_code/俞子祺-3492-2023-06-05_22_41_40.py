n=input()
ls=[]
for x in n:
    if n.count(x)==1:
        ls.append(x)
if len(ls)>0:
    print(x[0])
else:
    print("None")
