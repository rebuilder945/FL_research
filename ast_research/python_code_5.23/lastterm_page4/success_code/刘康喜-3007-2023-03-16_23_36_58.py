a=eval(input())
b=input().split(',')
if b[0]>b[1] or max(b)>len(a):
    print('error')
else:
    for i in range(b,c):
        del a[b]
    print(a)




