n = eval(input())
sum = sum(n)
avg = sum/len(n)
if avg == int(avg):
    print("%d"%(avg))
else:
    print("%.2f"%(avg))

