ls = eval(input())
x=sum(ls)/len(ls)
y=sum(ls)%len(ls)
if y == 0:
    print(int(x))
else:
    print("%.2f" % x)
