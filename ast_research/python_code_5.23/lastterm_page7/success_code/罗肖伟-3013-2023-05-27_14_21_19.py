s=input() or "ok"
count={}
while s!="ok":
    m,n=s.split()
    n=eval(n)
    count[m]=n
    s=input() or "ok"
countlist_keys=list(count.keys())
countlist_values=list(count.values())
sum=sum(countlist_values)
if "india" in countlist_keys:
    x="yes"
else:
    x="no"
print(countlist_keys)
print(countlist_values)
print(x)
print(sum)
