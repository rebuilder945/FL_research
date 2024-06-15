a=eval(input())
b,c=eval(input())
if c>len(a):
    print("error")
else:
    del a[b:c]
    print(a)
