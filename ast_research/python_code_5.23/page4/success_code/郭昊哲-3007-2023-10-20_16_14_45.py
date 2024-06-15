a=eval(input())
b,c=eval(input())
print(len(a))
if c+3>=len(a) or b>=c:
    print("error")
else:
    del a[b:c]
    print(a)
