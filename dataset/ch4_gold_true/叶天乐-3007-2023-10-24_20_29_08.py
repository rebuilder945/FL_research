ls1 = eval(input())
n,m = eval(input())
if n>len(ls1) or m>len(ls1):
    print("error")
else:
    del ls1[n:m]
    print(ls1)
