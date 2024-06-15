list1 = eval(input())
a = sum(list1)/len(list1)
if a - int(a) == 0:
    print(int(a))
else:
    print("%.2f"%a)
