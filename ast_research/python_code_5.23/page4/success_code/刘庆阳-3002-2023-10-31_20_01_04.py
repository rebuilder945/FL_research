def a(y):
    if sum(y)/len(y)!= 0:
        print("%.2f" %(sum(y)/len(y)))
    else:
        print("%d" %(sum(y)/len(y)))
sums=eval(input())
a(sums)
