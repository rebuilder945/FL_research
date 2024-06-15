a = eval(input())
# print(a,type(a))
for i in a:
    b = a.count(i)
    while b>1:
        a.remove(i)
        b-=1
print(a)

