a = list(eval(input()))
n = sum(a)
if n-int(n)==0:
    print(int(n))
else:
    print('%.2f'%n)
