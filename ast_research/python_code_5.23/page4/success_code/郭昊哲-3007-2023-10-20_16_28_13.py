a=eval(input())
b,c=eval(input())
if c+2>=len(a):
    print("error")
else:
    del a[b:c]
    print(a)
