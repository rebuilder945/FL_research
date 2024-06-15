lst = eval(input())
avg = sum(lst) / len(lst)
if avg == int(avg):
    print(int(avg))
else:
    print('%.2f' % avg)
