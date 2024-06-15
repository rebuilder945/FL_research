a=eval(input())
for i in a:
    if a.count(i)>1:
        a.remove(i)
    if a.count(i)==1:
        continue
print(a)
