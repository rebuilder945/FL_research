ls = eval(input())
x=sum(ls)/len(ls)
if x in int:
    print(x)
else:
    print("%.2f" % x)
