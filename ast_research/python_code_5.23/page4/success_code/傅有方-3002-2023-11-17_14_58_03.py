a=eval(input())
if sum(a)%len(a)==0:
    print(sum(a)/len(a))
else:
    print("%.2f"%(sum(a)/len(a)))
