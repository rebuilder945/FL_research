ls=eval(input())
n,m=eval(input())
ls2=[]
if n in ls:
    for i in ls:
        for x in range(n,m):
            if i not in range(n,m):
                ls2.append(i)
    print(ls2)
elif m in ls:
    for i in ls:
        for x in range(n,m):
            if i not in range(n,m):
                ls2.append(i)
    print(ls2)
else:
    print("error")
