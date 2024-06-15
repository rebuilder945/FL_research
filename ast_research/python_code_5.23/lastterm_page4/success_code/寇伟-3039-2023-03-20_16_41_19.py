ls = eval(input())
min_ls=min(ls)
max_ls=max(ls)
while max_ls in ls:
    ls.remove(max_ls)
while min_ls in ls:
    ls.remove(min_ls)
print(ls)

