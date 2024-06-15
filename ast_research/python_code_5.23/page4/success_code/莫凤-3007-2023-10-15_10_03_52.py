list=eval(input())
n,m=eval(input())
if n in list and m in list:
    del list[n:m]
    print(list)
else:
    print("error")
