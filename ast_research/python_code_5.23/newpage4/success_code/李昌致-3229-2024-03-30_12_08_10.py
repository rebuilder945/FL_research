a = eval(input())
b = []
c = len(a)
for i in a:
    amount = a.count(i)
    if amount == 1:
        b.append(i)
    else:
        pass
if b == []:
    print("False")
else:
    b.sort()
    d = ','.join(map(str,b))
    print(d)
