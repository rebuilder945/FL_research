list = eval(input())
n = sum(list)/len(list)
if sum(list)%len(list)==0:
    print(n)
else:
    print("%.2f"%n)


