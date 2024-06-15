lst = eval(input())
num = sum(lst)/len(lst)
if int(num) == float(num):
    print(int(num))
else:
    print("%.2f"%(num))

