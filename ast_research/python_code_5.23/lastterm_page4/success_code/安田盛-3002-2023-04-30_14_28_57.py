n=eval(input())
a=sum(n)/len(n)
if a-int(a)==0:
    print(int(a))
else:
    print("%.2f"%(a))



