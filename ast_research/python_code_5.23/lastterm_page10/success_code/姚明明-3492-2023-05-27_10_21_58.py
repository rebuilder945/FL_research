a=input()
ls=[]
for i in a:
    if i not in ls:
        ls.append(i)
if len(ls)==0:
    print("None")
else:
    print(ls[0])
