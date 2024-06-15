total_sum = 0
count = 0

while True:
    try:
        data = input()
        if data == "#":
            break
        value = int(data.strip())
        count += 1
        total_sum += value
    except ValueError:
        continue
result = '{} {}'.format(count, total_sum)
print(result)

