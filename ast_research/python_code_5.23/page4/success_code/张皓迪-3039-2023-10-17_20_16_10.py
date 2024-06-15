ls=eval(input())
for i in ls:
    b=max(ls)
    if i==b:
        ls.remove(i)
print(ls)
