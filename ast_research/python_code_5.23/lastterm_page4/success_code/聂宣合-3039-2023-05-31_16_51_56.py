lst=list(eval(input()))
maxn=max(lst)
minn=min(lst)
for i in range(len(lst)):
    if max(lst)==maxn:
        lst.remove(max(lst))
for i in range(len(lst)):
    if min(lst)==minn:
        lst.remove(min(lst))
print(lst)
