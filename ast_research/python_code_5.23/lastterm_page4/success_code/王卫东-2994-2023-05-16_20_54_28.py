a=list(eval(input()))
b,c=eval(input())
if abs(b)<=len(a):
    d=[a[b]]*c
    a=a+d
    print(a)
else:
    print("error")    
