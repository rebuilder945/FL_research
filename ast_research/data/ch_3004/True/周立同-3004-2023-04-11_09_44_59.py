lst=eval(input())
sulst=lst.copy()
for a in lst:
    if a==0 or a==1:
        sulst.remove(a)
    else:
        for i in range(2,a):
            b=a%i
            if a==0 or a==1 or b==0:
                sulst.remove(a)
                break
            else:
                continue
print(sulst)

