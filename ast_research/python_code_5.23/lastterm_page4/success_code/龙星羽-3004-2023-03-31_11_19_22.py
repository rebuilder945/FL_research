num=eval(input())
ls=[]
if 2 in num:
    ls.append(2)
for x in num:
    for i in range(2,x):
        if x%i==0:
            break
        else:
            ls.append(x)
print(ls)
    

