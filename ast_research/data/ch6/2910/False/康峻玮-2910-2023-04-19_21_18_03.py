h=eval(input())
N=eval(input())
i=0
while i<N:
    x = h*0.5**i
    y = h+2*x
    i=i+1
print("%.2f" % (y))

