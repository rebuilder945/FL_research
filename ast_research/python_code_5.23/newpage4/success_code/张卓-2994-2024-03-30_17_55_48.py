a=list(eval(input()))
d=[]
b,c=eval(input())
i=0
if b<len(a):
    while i<c:
        d.append(a[b])
        i+=1
    f=a+d
    print(f)
else: 
    print("error")
