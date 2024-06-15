a=list(eval(input()))
b,c=eval(input())
if b<=len(a):
    d=[a[b]]*c
    print(a+d)
else:
    print("error")

