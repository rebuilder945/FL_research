sear =input()
ab=input()

ub=ab.split(",")
m=ub[0]
n=ub[1]
m=int(m)
n=int(n)

search=list(sear.split(","))
if n-1>len(sear):  
    searchcopy=search.copy()
    x=list(search[n-1])
    del search[n-1] 
    y=x*(m+1)
    search=searchcopy+y
    print(search)
else:
    print("error")
