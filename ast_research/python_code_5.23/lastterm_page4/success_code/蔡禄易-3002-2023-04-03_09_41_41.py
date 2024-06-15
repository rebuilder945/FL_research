a = eval(input())
c = sum(a)/len(a)
if type(c)==float:
    print("%.2f"%c)
else:
    print(c)
