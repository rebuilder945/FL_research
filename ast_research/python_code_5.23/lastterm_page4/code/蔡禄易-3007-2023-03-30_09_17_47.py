lst = eval(input())
n,m = eval(input())
if m not in range(len(lst)):
    print("error")
elif n not in range(len(lst)):
    print("error")
else:
    print(del lst[n:m])
