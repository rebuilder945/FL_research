import ast

lst = input()
n_m = input()

lst = ast.literal_eval(lst)  # 将字符串转换为列表
n, m = map(int, n_m.split(","))

if n > len(lst) or m >= len(lst) or n > m:
    print("error")
else:
    del lst[n:m]
    print(lst)
