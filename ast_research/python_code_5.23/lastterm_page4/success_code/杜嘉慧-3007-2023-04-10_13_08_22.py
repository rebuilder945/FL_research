lst = eval(input())
n, m = [int(x) for x in input().split(',')]
length = len(lst)
if (n < 0 or n >= length) or (m < 0 or m >= length):
    print("error")
else:
    new = lst[:n] + lst[m:]
    print(new)

