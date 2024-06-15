def average(lst):
    a = sum(lst) / len(lst)
    if a == int(a):
        return int(a)
    else:
        return round(a, 2)

lst = eval(input())
print(average(lst))

