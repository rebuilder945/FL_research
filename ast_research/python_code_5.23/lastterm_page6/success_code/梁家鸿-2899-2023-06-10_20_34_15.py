b = input().split( )
n = int(b[0])
m = int(b[1])
a = ''
sum = 0
if n >= m or int(n) !=n or int(m)!=m or m - n <3:
    print('illegal input')
else:
    for i in range(n,m):
        for j in range(n,m) :
            for k in range(n,m) :
                if i!=j and i!=k and j!=k:
                        sum = i *100+j*10+k
                        if n > 99:
                            a = a + ' ' + str(sum)
    if a != '':
        print(a)
    else:
        print('illegal input')
