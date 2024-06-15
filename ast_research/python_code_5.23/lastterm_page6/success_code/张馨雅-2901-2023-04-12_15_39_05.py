line=0
sum=0
while True:
    n=input()
    if n=='#':
        break
    else:
        line+=1
        sum+=int(n)
print(line,sum)
