nums=eval(input())
ls=[]
ls1=[]
for x in nums:
    if x==1 or x==0:
        ls.append(x)
    else:
        for y in range(2,x):
            for z in range(2,x):
                if x==y*z:
                    ls.append(x)
for w in nums:
    if w not in ls:
        ls1.append(w)
print(ls1)
