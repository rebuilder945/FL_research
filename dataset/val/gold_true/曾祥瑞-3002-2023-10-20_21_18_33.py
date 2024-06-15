a=eval(input())
b=sum(a)
if b%len(a)==0:
    c=b/len(a)
    print(int(c))
else:
    print("%.2f"%(b/len(a)))
