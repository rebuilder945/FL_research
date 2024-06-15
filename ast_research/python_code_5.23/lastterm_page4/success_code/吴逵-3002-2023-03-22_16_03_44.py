lst = eval(input())
avg = sum(lst) / len(lst)
if avg.is_integer():
    print(int(avg))
else:
    print("%.2f" % avg)



