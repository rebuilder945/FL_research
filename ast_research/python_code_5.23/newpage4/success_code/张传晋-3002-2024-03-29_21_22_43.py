a = eval(input())
asum = sum(a)
lena = len(a)
avg = asum/lena
if avg%1==0:
    avg = int(avg)
    print(avg)
else:
    print("%.2f"%avg)


