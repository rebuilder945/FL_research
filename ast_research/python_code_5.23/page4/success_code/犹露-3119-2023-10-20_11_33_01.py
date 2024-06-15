a = eval(input())
# print(a,type(a))b
b = a[:]
for i in b:
    c= a.count(i)
    while c>1:
        a.remove(i)
        c-=1
print(a)

