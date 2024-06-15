h=eval(input())
N=eval(input())
i=0
y=h
while i<N:
    x = h*0.5**i
    y+= 2*x
    i=i+1
print("%.2f" % (y))

