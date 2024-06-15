count,sum=0,0
while True:
    n=input()
    if n!='#':
        count=count+1
        sum=sum+eval(n)
    else:
        break
print(count,sum)

