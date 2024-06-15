a=eval(input())
b=sum(a)
average=b/len(a)
Yaverage=b % len(a)
if Yaverage == 0:
    print(int(average))
else:
    pass
    print("%.2f" % (average))


