lst = eval(input())
num_zero = lst.count(0)
for num in range(num_zero):
    lst.remove(0)
    lst.append(0)
print(lst)
