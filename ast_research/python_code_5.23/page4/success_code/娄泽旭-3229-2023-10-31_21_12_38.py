a = eval(input())
b = []
for i in range(len(a)):
    if a.count(a[i]) == 1:
        b.append(a[i])
b.sort()
if b != []:
    c = ",".join(map(str,b))
    print(c)
else:
    print("error")
