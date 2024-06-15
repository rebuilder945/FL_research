count ,sum = 0,0
while 1:  
    n = input()
    if n != '#':
        count += 1
        sum += n
    else:
        break 
print(count,sum)       
