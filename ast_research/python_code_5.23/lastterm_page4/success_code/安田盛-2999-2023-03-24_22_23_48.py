str1=input().split()
n,m=map(int,input().split())
a=str1[n]
b=str1[m]
str1[m]=a
str1[n]=b
print(str1)

