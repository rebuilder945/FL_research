a=eval(input())
if sum(a)%len(a)==0:
    print(int(sum(a)/len(a)))
else:
    b=sum(a)/len(a)
    print("%.2f"%(b))
