numbers = eval(input())
n,m = eval(input())
l = len(numbers)
if -l <= n < l and -l <= m < l:
    del numbers[n:m]
else:
    print("error")

