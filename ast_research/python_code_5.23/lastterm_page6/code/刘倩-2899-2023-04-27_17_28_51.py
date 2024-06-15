n,m = map(int,input().split())

if n<0 or m>1000 or n>=m:
    print('illegal input')

else:
    for i in range(n,m):
        for j in range(n,m):
            for k in range(n,m):
                if i != j and i!= k and j!=k:
                    num = i*100 + j*10 + k
                    if num >=100 and num < 1000:
                        print(num,end=' ')
except ValueError:
    print("illegal input")
