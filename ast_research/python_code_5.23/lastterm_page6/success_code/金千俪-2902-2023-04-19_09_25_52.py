#n=int(input())
#a=2
#b=3
#d=1
#f=2
#sum = 0
#for i in range(n):
#    sum+=a/d
#    c=a+b
#    a=b
#    b=c
#    h=d+f
#    d=f
#    f=h
#print("%.4f"%sum)

n=int(input())
lst1=[2,3]
lst2=[1,2]
sum=2+3/2
for i in range(n-1):
    a=lst1[-1]+lst1[-2]
    lst1.append(a)
    b=lst2[-1]+lst2[-2]
    lst2.append(b)
    sum+=a/b
print("%.4f"%sum)
