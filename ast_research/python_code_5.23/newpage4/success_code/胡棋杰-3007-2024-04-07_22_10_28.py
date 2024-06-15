a=eval(input())
b,c=eval(input())
h=len(a)
if b<=c:
    max=c
    min=b
else :
    max=b
    min=c
if max<=h:
    del(a[min:max]) 
    print(a)
else :
    print("error")

