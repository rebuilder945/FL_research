sum=0
num=0
m=1
while(m):
    n=input()
    if n!='#':
        sum+=int(n)
        num+=1
    else:
        m=0
print(num,sum)
