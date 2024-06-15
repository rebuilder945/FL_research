lst=eval(input())
sulst=lst.copy()
for a in lst:
    for i in range(2,a):
        b=a%i
        if a==1 or b==0:
            sulst.remove(a)
            break
        else:
            continue
print(sulst)

