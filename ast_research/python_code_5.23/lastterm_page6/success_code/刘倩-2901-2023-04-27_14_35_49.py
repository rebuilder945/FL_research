total = 0
count = 0
while True:
    s = input().strip()
    if s == '#':
        break
    else:
        total += int(s)
        count += 1
print(f"{count} {total}")

