def amour(x):
    if x < 20:
        y = 6*x**2+1
        return y
    elif x in range(20,40):
        y = (3*x-60)**(1/2)
        return y
    elif x >= 40:
        y = 100/(x+1)
        return y
x = float(input())
#x 可能输入了大于等于 20 但小于 40 的值，
#但是在代码中，对于这种情况没有返回值，导致了 None 的返回。
y = amour(x)
print('{:.2f}'.format(y))
