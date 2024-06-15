a=list(eval(input()))
d=[]
b,c=eval(input())
i=0
e=a[b]
if b<len(a):
    while i<c:
        d.append(e)
        i+=1
    f=a+d
    print(f)
else: 
    print("error")
