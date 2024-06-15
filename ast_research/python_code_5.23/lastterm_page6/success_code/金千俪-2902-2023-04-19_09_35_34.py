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
if n>2:
    for i in range(n-2):
        a=lst1[-1]+lst1[-2]
        b=lst2[-1]+lst2[-2]
        lst1.append(a)
        lst2.append(b)
        sum+=a/b
    print("%.4f"%sum)
if n==2:
    print("3.5000")
if n==1:
    print("2.0000")
