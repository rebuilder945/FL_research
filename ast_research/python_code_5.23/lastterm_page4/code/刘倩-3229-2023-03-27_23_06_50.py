a = eval(input())
b = []
for x in a:
    if x not in b and b.count(x)=1:
        b.append(x)
        b.sort()
        print(b)
    else:
        print("False")

