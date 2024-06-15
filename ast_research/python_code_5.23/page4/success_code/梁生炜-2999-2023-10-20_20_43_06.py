ls1=input().split(" ")
m=eval(input());n=eval(input())
ls2=ls1.copy()
ls2[m]=ls1[n]
ls2[n]=ls1[m]
print(ls2)
