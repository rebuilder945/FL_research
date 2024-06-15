def su_shu(n):
    if n<=1:
        return 0
    else:
        ls=[]
        for i in range(2,n+1):
            if n%i==0:
                ls.append(i)
        if len(ls)==0:
            return 1
        else:
            return 0
lst=eval(input())
save=[]
for x in lst:
    if su_shu(x)==1:
        save.append(x)
print(save)
