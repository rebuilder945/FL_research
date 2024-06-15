lst = eval(input())
count = lst.count(0)
lst = [x for x in lst if x != 0]
lst.extend([0] * count)
print(lst)
