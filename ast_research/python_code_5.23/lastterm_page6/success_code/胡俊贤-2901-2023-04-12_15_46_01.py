sum=0
count=0
n=input()
while not n=='#':
    n=int(n)
    count+=1
    sum+=n
    n=input()
    print(count,sum)


