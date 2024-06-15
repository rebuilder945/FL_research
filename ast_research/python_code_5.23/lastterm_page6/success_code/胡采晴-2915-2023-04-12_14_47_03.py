n = int(input())
if n<153:
    print('none')
if n>=153:
    for i in range(153,n+1):
        a=i%10
        b=int(i%100/10)
        c=int(i/100)
        if a*a*a+b*b*b+c*c*c==i and i<1000:
            print(i)

    
    
    



