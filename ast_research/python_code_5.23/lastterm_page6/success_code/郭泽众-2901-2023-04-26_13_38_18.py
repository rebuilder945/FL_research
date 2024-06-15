sum = 0
fre = 0
while True:
    num = eval(input())
    if num == "#":
        break
    else:
        sum = sum + num
        fre = fre + 1

print("{} {}".format(sum,fre))
