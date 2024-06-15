import ast

lst = ast.literal_eval(input())
n, m = map(int, input().split(','))
if n < 1 or m > len(lst) or n >= m:
    print("error")
else:
    del lst[n-1:m+1]
    print(lst)
