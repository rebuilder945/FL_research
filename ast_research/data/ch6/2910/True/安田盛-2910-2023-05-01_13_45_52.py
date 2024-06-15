# h=eval(input())
# N=eval(input())
# if N ==1:
#     a=0
# else:
#     a=h+2*h*(0.5**(N-1))
#     c=0
#     for i in range(2,N):
#         c=c+2*h*0.5**(i-1)
# a=a+c
# print("%.2f"%(a))

h=eval(input())
N=eval(input())
if N==1:
    print("%.2f"%(h))
else:
    a=h
    for i in range(1,N):
        a+=2*h*0.5**i
    print("%.2f"%(a))

