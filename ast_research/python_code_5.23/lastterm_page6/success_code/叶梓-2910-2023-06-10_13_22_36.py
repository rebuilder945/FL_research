#h = eval(input())
#N = eval(input())
#num1 = 0
#if N == 1:
#    num1 = h
#else:
#    num1 += h
#    for x in range(2, N + 1):
#        H = h * 0.5 ** (x - 1)
#        num1 += H * 2
#print("%.2f" % num1)

h=eval(input())
N=eval(input())
num=0
if N==1:
    num=h
if N>1:
    num=h
    for x in range(2,N+1):
        H=2*h*(1/2)**(x-1)
        num+=H
    print("%.2f"%num)
