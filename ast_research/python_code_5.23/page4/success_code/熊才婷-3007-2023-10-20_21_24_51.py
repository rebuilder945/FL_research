ls=eval(input())
n,m=eval(input())
ls2=[]
if n>ls[-1] or m<=ls[0]:
    print("error")
else:
    for i in ls:
        for x in range(n,m):
            if i not in range(n,m):
                ls2.append(i)
    print(ls2)
