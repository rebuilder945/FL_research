a=eval(input())
n,m=eval(input())
if n<len(a) or n>=len(a):
    print("error")
else:
    b=[x for x in range(m)]
    print(a+b)
