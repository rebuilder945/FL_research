n=eval(input())
lst1=list(x for x in range(1,n+1))
lst2=lst1[1:]
lst2.append(lst1[0])
print(lst2)
