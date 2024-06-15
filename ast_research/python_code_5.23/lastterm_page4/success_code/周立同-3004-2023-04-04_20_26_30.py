lst=eval(input())
sulst=lst.copy()
for a in lst:
    for i in range(3,a):
        b=a%i
        if b==0:
            sulst.remove(a)
            break
        else:
            continue
print(sulst)

