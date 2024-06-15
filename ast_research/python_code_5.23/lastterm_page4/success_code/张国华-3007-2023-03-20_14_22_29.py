lst_str = input()
lst = eval(lst_str)
n, m = map(int, input().split(','))
if n < 0 or m >= len(lst) or n > m:
    print("error")
else:
    del lst[n:m]
    print(lst)
