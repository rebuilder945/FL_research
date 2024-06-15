l1 = list(map(int,input().split(",")))
n,m = eval(input())
l2 = l1.copy()
l3 = []
if len(l1) > n-1:
    a = l1[n-1]

    l4 = list(str(a))
    l5 = l4 * m
    l6 = l1 + l5
    l6 = list(map(int,l6))   
    print(l6)
else:
    print('False')
     
