def ling(y):
    z=[0]
    x=y.count(0)
    while 0 in y:
        y.remove(0)
    for i in range(x):
        y=y+z
    print(y)  
sums=eval(input())  
ling(sums)        
