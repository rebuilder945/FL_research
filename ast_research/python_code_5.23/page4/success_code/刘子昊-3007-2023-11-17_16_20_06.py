ls=eval(input())
n,m=eval(input())
if n>=m or n>=len(ls):
    print('error')
else:
    for i in range(m-n):
        del ls[n]
    print(ls)
