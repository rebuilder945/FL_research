a=eval(input().split(','))
n,m=eval((input))
if n>len(a)-1 or (-n)>len(a):
    print('error')
else:
    b=[a[n]*m]
    listul=a+b
    print(listul)
