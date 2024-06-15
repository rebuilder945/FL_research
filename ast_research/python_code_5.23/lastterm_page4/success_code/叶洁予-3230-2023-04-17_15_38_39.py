n=int(input())
if n>=1000:
    n=1000
    for i in range(100,n):
        bai=i//100
        shi=i%100//10
        ge=i%10
        if i==bai**3+shi**3+ge**3:
            print(i)
elif n>100:
    for i in range(100,n+1):
        bai=i//100
        shi=i%100//10
        ge=i%10
        if i==bai**3+shi**3+ge**3:
            print(i)
else:
    print('none')

