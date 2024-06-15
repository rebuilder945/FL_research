a=eval(input())
b,c=eval(input())
if b<=c and c<=len(a):
    for i in range(c-b):
        del a[b]
    print(a)
else:
    print("error")

