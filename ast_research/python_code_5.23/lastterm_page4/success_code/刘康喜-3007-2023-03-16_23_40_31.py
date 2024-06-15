a=eval(input())
b=input().split(',')
if int(b[0])>int(b[1]) or int(max(b))>len(a):
    print('error')
else:
    for i in range(int(b[0]),int(b[1])):
        del a[int(b[0])]
    print(a)




