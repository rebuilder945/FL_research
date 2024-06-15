lst=eval(input())
n,m=eval(input())
if n not in range(len(lst)) or m not in range(len(lst)):
    print("Error")
else:
    del lst[n:m]
    print(lst)
