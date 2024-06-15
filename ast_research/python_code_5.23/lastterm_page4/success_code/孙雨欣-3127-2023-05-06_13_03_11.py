a=eval(input())
ls1=[x for x in range(a)]
a=ls1[0]
for i in range(0,a-1):
    ls1[i]=ls1[i+1]
ls1[-1]=a
print(ls1)
