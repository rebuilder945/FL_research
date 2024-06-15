count,sum=0,0
while True:
    n=input()
    if n != '#':
        sum=sum+int(n)
        count += 1
    else:
        break
print(count,sum)
