def f1():
    m=lst[-1]+lst[-2]
    n=lst1[-1]+lst1[-2]
    inext=m/n
    lst.append(m)
    lst1.append(n)
    lst2.append(inext)

lst=[2,3]
lst1=[1,2]
lst2=[2/1,3/2]
i=int(input())
x=1
sum=0
for x in range(1,i+1):
    f1()
for y in range(0,i):
    sum +=lst2[y]
print('%.4f'%sum)
