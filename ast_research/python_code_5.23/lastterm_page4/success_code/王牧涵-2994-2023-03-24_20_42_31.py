import math
def liaowangwosunzi(y,m,n):
    if n!=math.floor(n):
        print('error');
    else:
        if n>=(-len(y)) and n<len(y):
            x=y[n];
        for i in range(m):
            y.append(x);
            print(y);
        else:
            print('error');
sums=list(eval(input()));
n,m=eval(input());
liaowangwosunzi(sums,n,m)

