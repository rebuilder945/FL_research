ls=eval(input())
total=sum(ls)
l=len(ls)
average=total/l
if type(average)==int:
    print("%d"%average)
else:
    print("%.2f"%average)


