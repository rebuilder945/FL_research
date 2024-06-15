sum = 0
fre = 0
while True:
    num = input()
    if num == "#":
        break
    else:
        sum = sum + int(num)
        fre = fre + 1

print("{} {}".format(sum,fre))
