lst = list(input().split(','))
n, m = map(int,input().split(','))
if n > len(lst) or m > len(lst):
    print("error")
else:
    lst = lst[n] + lst[m]
    print(lst)
