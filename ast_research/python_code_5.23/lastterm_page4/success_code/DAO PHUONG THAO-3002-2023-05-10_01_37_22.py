lst =eval(input())
m = sum(lst)
n = len(lst)
a = m/n
if a%1 == 0:
    print(int(a))
else:
    print('%.2f'%a)
