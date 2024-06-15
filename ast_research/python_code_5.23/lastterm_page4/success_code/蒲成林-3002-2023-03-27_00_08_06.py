def average(lst):
    a = sum(lst) / len(lst)
    if a == int(a):
        return int(a)
    else:
        return "{:.2f}".format(a)

lst = eval(input())
print(average(lst))

