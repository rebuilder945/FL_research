lst_str = input()
lst = eval(lst_str)
n, m = map(int, input().split(','))
if n >= 0 and n < len(lst) and m >= 0 and m < len(lst) and n <= m:
    del lst[n:m]
    print(lst)
else:
    print("error")
