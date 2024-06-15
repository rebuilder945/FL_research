a=eval(input())
b,c=eval(input())
if c > len(a)-1 or b <0 :
    print("error")
else:
    del a[b:c]
    print(a)
