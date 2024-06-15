total = 0
count = 0
flag = False
while not flag:
    s = input()
    if s == "#":
        flag = True
    else:
        total += int(s)
        count += 1
print(count,total )
