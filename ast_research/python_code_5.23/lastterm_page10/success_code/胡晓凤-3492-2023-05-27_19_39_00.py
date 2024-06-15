a=list(input())
ls=[]
for i in a:
    if a.count(i)==1:
        ls.append(i)
if ls==[]:
    print("None")
else:
    print(ls[0])
