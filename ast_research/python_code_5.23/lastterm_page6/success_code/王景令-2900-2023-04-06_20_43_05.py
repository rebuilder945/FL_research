def aaa(n):
    m = []
    if n  == 2:
        return 1
    for i in range(2,n):
        c = n % i
        m.append(c)
    if 0 in m:
        return 0
    else:
        return 1




a = eval(input())
b = []
if a <= 0:
    print('illegal input')
elif int(a) != a:
    print('illegal input')
else:
    if a == 2:
        b.append(str(2))
    for i in range(2,a):
        if str(i) == str(i)[::-1] and aaa(i) == 1:
            b.append(str(i))

print(' '.join(b))
        

