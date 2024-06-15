def ave(x):
    d = sum(x)/len(x)
    if int(d) == d:
        print(int(d))
    else:
        print("%.2f"%(d))
a = eval(input())
