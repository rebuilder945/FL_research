ls1=input().split(" ")
m,n=eval(input())
a=" "
a=ls1[m]
ls1[m]=ls1[n]
ls1[n]=a
print(ls1)
