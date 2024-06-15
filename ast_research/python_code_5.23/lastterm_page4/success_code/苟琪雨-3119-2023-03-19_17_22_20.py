a=eval(input())
for i in a:
    while a.count(i)>1:
        a.pop(i)
print(a)
