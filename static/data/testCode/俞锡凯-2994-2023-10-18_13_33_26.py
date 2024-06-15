a=list(eval(input()))
n,m=eval(input())
c=len(a)
if n>c:
    print("error")
else:
    b=a.copy(n)
    for b in range(m):
        a.append(b)
        print(a)

        
    


