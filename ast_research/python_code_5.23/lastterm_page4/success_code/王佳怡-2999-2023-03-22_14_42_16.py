l=input()
l1=l.split()
n,m=eval(input())
a=l1[n]
l1[n]=l1[m]
l1[m]=a
print(l1)

