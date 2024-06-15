lst=eval(input())
max_num=max(lst)
min_num=min(lst)
for num in lst:
    if num == max_num or min_num:
        lst.remove(num)
print(lst)


