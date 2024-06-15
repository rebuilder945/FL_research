num = input().split(",")
n,m = eval(input())
if n < 0 or n >= len(num):
    print("error")
else:
    a = num[n]
    num += [a]*m
    list = [int(x) for x in num]
    print(list)
