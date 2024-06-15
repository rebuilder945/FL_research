list = eval(input())
n = sum(list)/len(list)
if sum(list)%len(list)==0:
    print("%d"%n)
else:
    print("%.2f"%n)


