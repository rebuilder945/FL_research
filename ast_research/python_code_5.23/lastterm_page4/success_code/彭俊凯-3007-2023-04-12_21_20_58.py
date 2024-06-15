a=eval(input())
b,c=eval(input())
if b or c>len(a):
    print('error')
else:
    del a[b:c]
    print(a)

