def cacluate(n):
    if n<20:
        word=6*(n**2)+1
    elif 20<=n<40:
        word=(3*n-60)**0.5
    else:
        word=100/(n+1)
    return word
    
x=eval(input())
deal=cacluate(x)
print("%.2f"%deal)
