n=eval(input())
lst=list(range(1,n+1))
lst1=lst.copy()
lst1[n-1]=lst[0]
lst2=lst1.append(1)
print(lst2)
