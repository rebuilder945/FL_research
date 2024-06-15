def main(x):
    if x<20:
        return 6*x**2+1
    elif x>=20 and x<40:
        return (3*x-60)**0.5
    else:
        return 100/(x+1)

x=eval(input())
print('{:.2f}'.format(main(x)))
