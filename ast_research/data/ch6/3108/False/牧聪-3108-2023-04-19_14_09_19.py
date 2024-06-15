a=eval(input())
m=""
for x in a:
    t=str(x)
    m=m+t
lst=list(m)
for i in [chr(i)for i in range(97,123)]:
    if lst.count(i)>0:
        print(i,lst.count(i))

