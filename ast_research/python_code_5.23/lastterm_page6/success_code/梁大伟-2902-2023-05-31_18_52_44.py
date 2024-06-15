def feb(n):
    lst1=[1,1]
    for i in range(n):
        lst1.append(lst1[i]+lst1[i+1])
    return lst1
n=eval(input())
ls1=feb(n+1)
ls2=feb(n)
s=0
for i in range(n):
    s=s+ls1[i+2]/ls2[i+1]
print('%.4f'%(s))
