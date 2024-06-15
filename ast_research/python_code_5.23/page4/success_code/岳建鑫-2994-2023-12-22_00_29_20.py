data = input().split(",")
n, m = map(int, input().split(","))

if abs(n) > len(data):
    print("error")
else:
    if n < 0:
        n += len(data)
    element = data[n-1]
    data += [element] * m
    print(data)

