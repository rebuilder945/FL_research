ls1 = eval(input())
n,m = map(int,input().split(","))
if n > len(ls1)-1 or m > len(ls1)-1:
    print("error")
else:
    del ls1[n:m]
    print(ls1)
