lst=eval(input())
n=max(lst)
m=min(lst)
tep=lst.copy()
for num in lst:
    if num==n or num==m:
        tep.remove(num)
print(tep)
