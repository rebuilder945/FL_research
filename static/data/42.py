a = 100.123456
#错误写法：b = f'{a:.f2}'
b = f'{a:.2f}'
#或者也是可以使用round
c = round(a,2)
print(b,c)