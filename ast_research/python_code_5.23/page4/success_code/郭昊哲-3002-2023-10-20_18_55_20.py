a=eval(input())
b=sum(a)
c=b/(len(a))
if c//1==c:
    print(int(c))
else:
    print("%.2f"%(c))
