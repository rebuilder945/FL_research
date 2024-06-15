def av(lst):
    return "{:.2f}".format(sum(lst)/len(lst))
lst = eval(input())
print(av(lst))
