lst = eval(input())
a = sum(lst) / len(lst)
if sum(lst) / len(lst) == 0:
    print("%d" % a)
else:
    print("%.2f"%a)
