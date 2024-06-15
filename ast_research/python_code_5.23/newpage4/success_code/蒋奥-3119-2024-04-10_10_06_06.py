a = eval(input())
b=a.copy
for i in a:
    while a.count(i)>1:
        b.remove(i)
print(b)
    



