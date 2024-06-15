list1 =input()
a = eval(list1)
b = sum(a)/len(a)
if b//1 == 0:
    print(int(b))
else:
    print("%.2f"%b)
