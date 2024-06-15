lis = eval(input())
count = []
for x in lis:
    count.append(lis.count(x))
max_count = max(count)
for i in range(max_count):
    for x in lis:
        if lis.count(x) == 1:
            continue
        else:
            lis.remove(x)
print(lis)

