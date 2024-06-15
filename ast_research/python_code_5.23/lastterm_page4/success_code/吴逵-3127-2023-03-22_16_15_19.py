n = int(input())
lst = list(range(1, n+1))
new_lst = lst[1:] + lst[:1]
print(new_lst)

