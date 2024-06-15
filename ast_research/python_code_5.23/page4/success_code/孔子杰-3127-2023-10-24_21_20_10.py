n=eval(input())
lst1=[x for x in range(1,n+1,1)]
lst2=[]
a=lst1[0]
lst2.append(a)
lst1.remove(a)
lst=lst1+lst2
print(lst)

