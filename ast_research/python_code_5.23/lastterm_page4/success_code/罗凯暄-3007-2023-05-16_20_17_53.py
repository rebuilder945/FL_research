ist = eval(input())
n,m = eval(input())
if n<= 0 or m >= len(ist) or n > m:
    print('error')
else:
    del ist[n:m]
    print(ist,sep="")
