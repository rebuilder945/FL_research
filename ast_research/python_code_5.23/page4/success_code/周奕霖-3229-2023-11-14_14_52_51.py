a = eval(input())
a.sort()
b = []
for x in a:
    if a.count(x) == 1:
        b.append(x)
b = ",".join(str(i) for i in b)
if len(b)==0:
    print("Flase")
else:
    print(b)



