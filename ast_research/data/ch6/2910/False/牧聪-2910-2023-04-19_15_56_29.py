h = int(input())
a = h
n = int(input())
length = []

for x in range(n):
    h = h / 2
    length.append(h)

b = sum(length)
total_distance = 2 * b + a 
print("%.2f" % total_distance)

