n = eval(input())
a = ''
if n <= 1 or int(n) != n:
    print('illegal input')
else:
    for x in range(2,n+1):
        if x == 2:
           a = a + ' ' + str(x)
        else:
            for i in range(2,x):
                if x % i ==0:
                    break
            else:
                if str(x)[::-1] == str(x):
                    a = a + ' ' + str(x)
print(a)
