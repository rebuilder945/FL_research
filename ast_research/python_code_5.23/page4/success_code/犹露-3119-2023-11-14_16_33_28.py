a = eval(input())
# print(a,type(a))b

for i in a:
    c= a.count(i)
    while c>1:
        a.remove(i)
        c-=1
print(a)

