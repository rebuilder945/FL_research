lst = eval(input())
x = sum(lst)/len(lst)
if x%1 > 0:
    print('%.2f'%x)
else:
    print(x)
