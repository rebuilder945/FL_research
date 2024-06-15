n=input()
ls=[]
ls2=[]
ls3=[]
for i in n:
    ls.append(i)
for k in ls:
    if k not in ls2:
        ls2.append(k)
    if k in ls2:
        ls3.append(k)
if ls3!=[]:
    print(ls3[0])
else:
    print("None")

