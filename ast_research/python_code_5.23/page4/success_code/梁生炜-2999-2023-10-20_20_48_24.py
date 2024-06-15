ls1=input().split(" ")
ls2=input().split(" ")
m=ls2[0],n=ls2[1]
ls2=ls1.copy()
ls2[m]=ls1[n]
ls2[n]=ls1[m]
print(ls2)
