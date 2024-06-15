lst = eval(input())
n, m = map(int, input().split(','))

if n > m or m >= len(lst):
    print("error")
else:
    del lst[n:m]
    print(lst)
