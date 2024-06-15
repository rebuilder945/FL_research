a=list(eval(input()))
b,c=eval(input())
if b >= len(a) or b< -len(a):
    print("error")
else :
    d=a[b]
    for i in range(c):
        
        a.append(d)
    print(a)
    
