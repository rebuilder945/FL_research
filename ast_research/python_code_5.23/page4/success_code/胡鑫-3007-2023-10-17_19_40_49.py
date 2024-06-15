lst = eval(input())
n,m = eval(input())
if n > m or n<0 or m > len(lst):
    print("error")
else:
    del lst[n:m]
    print(lst)
