list=eval(input())
n,m=eval(input())
if n in list or m in list:
    del list[n:m]
    print(list)
else:
    print("error")
