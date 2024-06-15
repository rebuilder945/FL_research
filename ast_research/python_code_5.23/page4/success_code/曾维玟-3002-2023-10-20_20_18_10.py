lst = eval(input())
a = sum(lst)
b = len(lst)
c = a/b
if c%1 == 0:
    print(int(c))
else:
    print('%.2f'%c)
