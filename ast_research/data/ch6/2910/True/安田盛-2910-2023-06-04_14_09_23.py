h=eval(input())
N=eval(input())
if N==1:
    print(h)
else:
    s=h
    for i in range(1,N):
        s+=(0.5)**i*h*2
    print("{:.2f}".format(s))





    





