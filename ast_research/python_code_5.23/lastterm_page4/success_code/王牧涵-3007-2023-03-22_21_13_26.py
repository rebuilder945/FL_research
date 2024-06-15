sums= eval(input())
n,m = input().split(',')
n=int(n)
m=int(m)
if n<len(sums) and m<len(sums):
    if n<m:
        del sums[n:m]
        print(sums)
    else:
        del sums[m+1:n+1]
else:
    print('error')

