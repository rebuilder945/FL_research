ls=eval(input())
average=sum(ls)/len(ls)
a=str(average)
a=a.split(".")
if int(a[1])==0:
    print(a[0])
else:
    print("{:.2f}".format(average))
