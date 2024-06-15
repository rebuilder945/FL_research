a = eval(input())
for x in a:
    if a.count(x)>1:
        for i in range(a.count(x)):
            a.remove(x)
a.sort()

if len(a)>0:
    a = str(a)
    print(a)
else:
    print("False")
