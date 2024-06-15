m=list(input().split(","))
c=list(eval(input()))
lst=[[m[i],c[i]] for i in range(len(m))]
lst1=sorted(lst,key=lambda x:x[1])
print(lst1)

