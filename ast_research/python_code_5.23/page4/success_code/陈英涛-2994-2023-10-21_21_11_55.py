l1 = eval(input())
n,m = eval(input())
if n < len(l1):
    del l1[n]
    a = l1[n]
    l2 = []
    l2.append(a)
    l3 = l2 * m
    l4 = l1 + l3
    print(l4)
else:
    print("error")


