ls1=input().split(" ")
ls2=input().split(" ")
m=ls2[0],n=ls2[1]
ls3=ls1.copy()
ls3[m]=ls1[n]
ls3[n]=ls1[m]
print(ls3)
