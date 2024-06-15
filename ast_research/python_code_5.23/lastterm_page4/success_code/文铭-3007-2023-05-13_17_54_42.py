ls = eval(input())
n,m = eval(input())
if n in range(len(ls)) and m in range(len(ls)):
    del ls[n:m]
    print(ls)
else:
    print("error")
