search=eval(input())
a=max(search)
b=min(search)
for i in search:
    if i ==a or i == b:
        search.remove(a)
        search.remove(b)
print(search)
