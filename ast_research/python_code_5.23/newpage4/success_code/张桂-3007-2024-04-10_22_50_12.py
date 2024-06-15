lst = eval(input())
n,m = eval(input())
if n in range(len(lst)) and m in range(len(lst)):
    del lst[n:m]
    print(lst)
else:
    print("error")
