ls=eval(input())
total=sum(ls)
average=total/3
if type(average) is int:
    print(int(average))
else:
    print("%.2f"%average)


