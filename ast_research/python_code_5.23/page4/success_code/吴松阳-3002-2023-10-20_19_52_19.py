lst = eval(input())
average = sum(lst)/len(lst)
if average%1 == 0:
    print(int(average))
else:
    print('{:.2f}'.format(average))
