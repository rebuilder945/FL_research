ls=eval(input())
for i in ls:
    b=max(ls)
    c=min(ls)
    if i==b:
        ls.remove(i)
    if i==c:
        ls.remove(i)
print(ls)
