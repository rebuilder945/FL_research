# str1=input().split()
# n,m=map(int,input().split())
# a=str1[n]
# b=str1[m]
# str1[m]=a
# str1[n]=b
# print(str1)

ls=input().split()
n,m=map(int,input().split())
ls[n],ls[m]=ls[m],ls[n]
print(ls)

