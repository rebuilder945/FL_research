a=input().split(",")
n,m=eval(input())
if n>=len(a) or n<=-len(a):
    print("error")
else:
    b=[a[n] for i in range(m)]
    print(list(map(int,(a+b))))
