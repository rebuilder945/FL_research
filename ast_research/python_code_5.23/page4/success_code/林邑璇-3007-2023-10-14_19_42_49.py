a=eval(input())
b,c=eval(input())
if b<=c and c<=len(a):
    for i in range(b,c):
        del a[i]
    print(a)
else:
    print("error")
