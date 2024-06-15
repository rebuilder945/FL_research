n,m = map(int,input().split())

if n<0 or m>9 or n>=m or m-n<3:
    print('iellgal input')

for i in range(n,m):
    for k in range(n,m):
        for j in range(n,m):
            if i != k !=j:
                num = i*100 + k*10 + j
                if num>=100 and num<1000:
                    print(num,end=' ')
