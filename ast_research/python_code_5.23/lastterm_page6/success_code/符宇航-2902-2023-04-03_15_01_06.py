n = eval(input())
q1 = 1
q2 = 2
if n<2:
    print('2.000')
elif n == 2:
    print('2.500')
else:
    numlist = []
    for i in range(n-1):
        q = q1+q2
        numlist.append(q/q2)
        q1 = q2
        q2 = q
    s = sum(numlist) + 2
    print('%.4f'%s)



