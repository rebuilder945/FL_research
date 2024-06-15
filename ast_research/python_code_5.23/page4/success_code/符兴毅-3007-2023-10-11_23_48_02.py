a = eval(input())
b,c = eval(input())
try:
    del a[b:c]
except:
    print('error')
else:
    print(a)

