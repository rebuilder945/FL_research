h=eval(input())
N=eval(input())
chu=h
while N>1:
    h=h/2
    chu+=2*h
    N-=1
print("{:.2f}".format(chu))

