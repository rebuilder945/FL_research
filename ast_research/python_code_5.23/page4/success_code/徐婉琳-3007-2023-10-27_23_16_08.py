c=eval(input())
n,m=eval(input())
k=len(c)
if n>=0 and m<k:
    s1=c[:n]
    s2=c[m:k]
    s=s1+s2    
    print(s)
if n>=k and m>=n:
    print("error")
