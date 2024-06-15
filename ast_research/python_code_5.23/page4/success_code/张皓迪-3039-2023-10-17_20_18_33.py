ls=eval(input())
b=max(ls)
c=min(ls)
for i in ls:
    if i==b or i==c:
        ls.remove(i)   
print(ls)
