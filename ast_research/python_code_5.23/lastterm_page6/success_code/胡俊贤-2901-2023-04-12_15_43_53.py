sum=0
count=0
n=eval(input())
while not n=='#':
    count+=1
    sum+=n
    n=eval(input())

    print(count,sum)


