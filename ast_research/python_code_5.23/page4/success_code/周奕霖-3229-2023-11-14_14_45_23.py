a = eval(input())
a.sort()
b = []
for x in a:
    if a.count(x) == 1:
        b.append(x)
        b = int (b)
        print(b)
    else:
        print("Flase")


