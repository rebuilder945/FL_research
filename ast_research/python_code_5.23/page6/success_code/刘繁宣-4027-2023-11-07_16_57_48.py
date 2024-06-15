sum,cot = 0,0
while True:
    n = input()
    if n !='#':
        sum += eval(n)
        cot += 1
    else:
        break
print(cot,sum)
