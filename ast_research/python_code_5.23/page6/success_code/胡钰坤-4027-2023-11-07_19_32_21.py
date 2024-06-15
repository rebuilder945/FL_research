cont = 0
sum = 0
while True:
    n = input()
    if n != '#':
        cont += 1
        sum += int(n)
    else:
        break
print(cont,sum)
