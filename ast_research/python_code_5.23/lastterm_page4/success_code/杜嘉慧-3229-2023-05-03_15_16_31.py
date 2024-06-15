lst = eval(input())
new = []
for x in lst:
    if lst.count(x) == 1:
        new.append(x)
        new.sort()
        print(new)
else:
    print("False")




