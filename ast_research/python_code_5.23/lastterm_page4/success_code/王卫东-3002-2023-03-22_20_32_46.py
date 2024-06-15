a = eval(input())
c =sum(a)/len(a)
if sum(a)%len(a)==0:
    print("%d"%(c))
else:
    print("%.2f"%(c))

