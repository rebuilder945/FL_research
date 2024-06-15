a = eval(input())
b,c = eval(input())
if b>len(a) or c>len(a):
    print('error')
else:
    try:
        del a[b:c]
    except :
        print('error')
    else:
        print(a)

