n=eval(input())
lis=[]
for x in range(100,n+1):
    ge=x%10
    shi=(x-ge)/10%10
    bai=(x-ge-shi*10)/100
    if ge**3+shi**3+bai**3==x:
        if x<=999:
            print(x)
            lis.append(x)
if not lis:
    print('none')
