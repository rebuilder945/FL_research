from os import remove


a=eval(input())
b,c=eval(input())
length=len(a)
if b>=length:
    print("error")
else:
    del a[b:c]
    print(a)


