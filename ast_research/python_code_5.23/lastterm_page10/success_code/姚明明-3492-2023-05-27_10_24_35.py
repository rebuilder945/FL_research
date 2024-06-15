a=input()
ls1=list(a)
ls=[]
for i in ls1:
    if i not in ls:
        ls.append(i)
if len(ls)==0:
    print("None")
else:
    print(ls[0])
