def pingjun(y):
    a=sum(y)/len(y)
    if a%1==0:
        print(int(a))
    else:
        print("%.2f" % a)
sums=eval(input())
pingjun(sums)





