l = eval(input())
l1 = []
for n in l:
    if l.count(n)==1:
        l1.append(n)
        l1.sort()
        print(l1)
    else:
        print("False")
