lst=eval(input())
lst.sort(reverse=1)
res=0
for x in lst:
    res*=10
    res+=x
print(res)
