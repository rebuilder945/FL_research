def a(lst, n, m):
    if n > len(lst) or m > len(lst) or n > m:
        print("error")
    else:
        del lst[n:m+1]
        print(lst)

lst = eval(input())
n, m = map(int, input().split(','))
a(lst, n, m)

