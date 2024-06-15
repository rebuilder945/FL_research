a=eval(input())
for x in list(a):
    if a.count(x)>1:
        a.remove(x)
print(a)
