l1 = list(map(int,input().split(",")))
n,m = eval(input())
l2 = l1.copy()
if len(l1) > n-1:
    a = l1[n]
    l3 = [a]*m
    l4 = l1 + l3
    print(l4)
else:
    print("error")
    

     
