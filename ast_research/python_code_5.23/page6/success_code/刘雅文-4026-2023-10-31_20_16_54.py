from re import A


n=eval(input())
a=1
b=2
list1=[]
for x in range(n):
    p=b/a
    c=a+b
    a=b
    b=c
    list1.append(p)
print('%.4f'%(sum(list1)))
