ls1 = list(map(int,input().split(",")))
n,m = eval(input())
if n>=len(ls1):
    print("error")
else:
    a = ls1[n]
    while m>0:
        ls1.append(a)
        m-=1
    print(ls1)
