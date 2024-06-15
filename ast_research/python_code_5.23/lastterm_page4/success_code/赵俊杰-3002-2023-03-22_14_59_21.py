ls=eval(input())
total=sum(ls)
l=len(ls)
average=total/l
if type(average) is int:
    print("%.0f"%average)
else:
    print("%.2f"%average)


