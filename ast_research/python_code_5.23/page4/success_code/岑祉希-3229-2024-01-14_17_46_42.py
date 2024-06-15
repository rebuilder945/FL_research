
n = eval(input())
m = []
x = False
for a in n:
    if n.count(a) == 1:
        m.append(a)
        x = True
m.sort()
result = ",".join(str(num) for num in m)
if x:
    print(result)
else:
    print("False")


