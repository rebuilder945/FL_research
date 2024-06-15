n=eval(input())
if n<100 or n>1000:
    print('none')
for i in range(100,n+1):
    a=i%10#个位
    b=int(i%100//10)#十位
    c=int(i//100)#百位
    if a*a*a+b*b*b+c*c*c==i:
        print(i)
    else:
        print('none')
