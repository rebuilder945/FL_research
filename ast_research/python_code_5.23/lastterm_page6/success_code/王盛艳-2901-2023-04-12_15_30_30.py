sum = 0
x = 0
y = 1
while (y):
    s = input()
    if s != "#":
        x += 1
        sum += int(s)
    else:
        y = 0
print(x,sum)
