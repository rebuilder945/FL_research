a = eval(input())
c = sum(a)/len(a)
avg = int(c)
if c > avg:
    print("%.2f"%c)
else:
    print(avg)
