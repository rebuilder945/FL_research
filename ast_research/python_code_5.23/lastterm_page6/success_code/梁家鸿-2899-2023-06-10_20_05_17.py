n,m = eval(input())
a = ''
sum = 0
if n >= m or int(n) !=n or int(m)!=m:
    print('illegal input')
else:
    for i in range(n,m):
        sum += i * 100
        for j in range(n,m) and i!=j:
            sum += j * 10
            for k in range(n,m) and i!=k and j!=k:
                sum += k
                a = a + ' ' + str(sum)
                sum = 0
if a != '':
    print(a)
else:
    print('illegal input')
