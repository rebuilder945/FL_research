def pingjun(y):
    a=sum(y)/len(y)
    if a-int(a)>0:
     print("%.2f" %(a))
    elif a-int(a) == 0:
        print(int(a))
sums=eval(input())
pingjun(sums)

