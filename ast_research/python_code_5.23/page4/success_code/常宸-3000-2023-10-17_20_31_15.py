a = eval(input())
avg = sum(a)/len(a)
if (avg%1==0):
    print(int(avg))
else:
    print("%.2f"%(avg))
