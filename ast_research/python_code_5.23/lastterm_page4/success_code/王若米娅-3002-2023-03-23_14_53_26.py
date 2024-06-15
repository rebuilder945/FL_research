a=eval(input())
c=sum(a)/len(a)

if c-int(c)==0:
    print(int(c))
else:
    print("%.2f"%(c))


