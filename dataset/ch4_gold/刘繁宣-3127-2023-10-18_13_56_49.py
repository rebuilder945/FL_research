n=eval(input())
ls=[x for x in range(1,1+n)]
ls[0],ls[-1]=ls[-1],ls[0]
print(ls)
