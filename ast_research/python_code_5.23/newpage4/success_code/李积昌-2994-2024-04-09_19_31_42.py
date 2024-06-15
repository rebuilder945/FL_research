a=list(eval(input()))
b,c=eval(input())
if b >= len(a) or b< -len(a):
    print("error")
else :
    for i in range(c):
        d=a[b]
        a.append(d)
    print(a)
    
