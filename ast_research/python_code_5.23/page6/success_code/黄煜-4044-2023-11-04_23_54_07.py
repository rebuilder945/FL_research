a=eval(input())
for i in range(100,a-2):
    a=i%10
    b=int(i%100/10)
    c=int(i/100)
    if a*a*a+b*b*b+c*c*c==i:
        print(i)
    
