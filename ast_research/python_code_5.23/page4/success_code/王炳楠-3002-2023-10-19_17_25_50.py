l=eval(input())
a=sum(l)/len(l)
if a==int(a):
    print(int(a))
else:
    print("%.2f"%(a))
