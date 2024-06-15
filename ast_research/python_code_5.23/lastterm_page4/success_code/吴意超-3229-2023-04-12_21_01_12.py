a = eval(input())
b = set(a)
c = []
for i in b:
    if(a.count(i) == 1):
        c.append(i)
c.sort()
if(c == []):
    print("False")
else:
    c = list(map(str,c))
    print(",".join(c))
