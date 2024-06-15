n = eval(input())
m=sum(n)/len(n)
if m==int(m):
    print("%.0f"%(m))
else:
    print("%.2f"%(m))
