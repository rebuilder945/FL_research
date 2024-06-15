a=eval(input())
if sum(a)%len(a)==0:
    print(int(sum(a)/len(a)))
else:
    print("%.2f"%(sum(a)/len(a)))

