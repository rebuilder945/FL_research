count,sum = 0,0
while True:
    n = eval(input())
    if n != '#':
        count+=1
        sum+=eval(n)
    else:
        break
print(count,sum)

