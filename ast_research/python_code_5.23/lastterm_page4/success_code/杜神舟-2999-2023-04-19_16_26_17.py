lst1=eval(input()).split()
n,m=eval(input())
lst2=lst1.copy()
lst2[n-1]=lst1[m-1]
lst2[m-1]=lst1[n-1]
print(lst2)
