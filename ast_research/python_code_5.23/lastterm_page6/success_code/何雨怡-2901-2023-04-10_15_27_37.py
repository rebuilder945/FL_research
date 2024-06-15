n=input()
counter=0
sum=0
while n!='#':
    sum=sum+int(n)
    n=input()
    counter+=1
if n=='#':
    print(counter,sum)

