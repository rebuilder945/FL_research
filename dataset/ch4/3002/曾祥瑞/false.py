a=eval(input())
b=sum(a)
if b%len(a)==0:
    c=b/len(a)
    print(c)
else:
    print("%.2f"%(b/len(a)))
