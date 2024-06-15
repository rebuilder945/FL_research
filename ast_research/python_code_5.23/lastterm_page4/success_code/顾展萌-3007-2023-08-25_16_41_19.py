lst = eval(input())
n,m = input().split(",")
n = int(n)
m = int(m)
if n > m or n <0 or m<=0 or n >len(lst) or m > len(lst):
    print("error")
else:
    del lst[n:m]
    print(lst)
