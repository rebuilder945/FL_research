lst = eval(input())
max_num = max(lst)
min_num = min(lst)
nums = lst.copy()
for num in nums:
    if num == max_num or num == min_num:
     lst.remove(num)
print(lst)


