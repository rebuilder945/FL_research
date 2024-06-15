a=input()
n,m=map(int,input().split())
lst1=a.split()
lst2=lst1.copy()
lst2[m]=lst1[n]
lst2[n]=lst1[m]
print(lst2)
