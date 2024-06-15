Z=eval(input())
lst1=[x for x in range(1,Z+1)]
m=lst1[1:-1]
result=m+[lst1[-1],lst1[0]]
print(result)
