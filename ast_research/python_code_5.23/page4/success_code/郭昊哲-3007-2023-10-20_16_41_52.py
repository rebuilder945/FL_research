a=eval(input())
b,c=eval(input())
if c+1>=len(a) or b>a:
    print("error")
else:
    del a[b:c]
    print(a) 
