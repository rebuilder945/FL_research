n=eval(input())
lis=[]
if n>100 and n<1000:
    for i in range(100,n+1):
        a=i%10#个位
        b=int(i%100//10)#十位
        c=int(i//100)#百位
           lis.append(i)
        if a*a*a+b*b*b+c*c*c==i and lis:
            print(i)
        else:
            print('none')        
else:
    print('none')
