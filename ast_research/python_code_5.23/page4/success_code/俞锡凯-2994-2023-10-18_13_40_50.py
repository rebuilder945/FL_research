a=list(eval(input()))
n,m=eval(input())
c=len(a)
if n>c:
    print("error")
else:
        b=a[n]
        while b in range(m):
            a.append(b)
            break
        print(a)

        
    


