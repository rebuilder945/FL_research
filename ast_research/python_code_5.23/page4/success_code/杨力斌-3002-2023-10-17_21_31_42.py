a = eval(input())
b = sum(a)
c = len(a)
average = str(b/c)
if average[-1] in "0":
    d = int(average)
    print(d)
else:
    average = eval(average)
    print("%.2f"%average)
