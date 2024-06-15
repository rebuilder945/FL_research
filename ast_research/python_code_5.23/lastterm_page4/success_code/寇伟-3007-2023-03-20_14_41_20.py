ls1=eval(input())



n,m=map(int,input().split(','))

# if m==n:
#     del ls1[m-1]

if 0<=n<m<=len(ls1):
    del ls1[n:m]
    print(ls1)

else:
    print('error')




