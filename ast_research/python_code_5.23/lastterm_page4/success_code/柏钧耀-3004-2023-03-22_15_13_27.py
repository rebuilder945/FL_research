a=eval(input())
n=max(a)
for i in range(2,n):
    if i%range(2,i)==0:
        a.remove(i)
    else:
        pass
    print(a)

