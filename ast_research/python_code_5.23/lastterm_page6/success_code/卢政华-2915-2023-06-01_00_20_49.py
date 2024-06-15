num = int(input())
a = []
for i in range(100, num+1):
    a1 = i // 100
    a2 = (i // 10) % 10
    a3 = i % 10
    if a1**3+a2**3+a3**3 == i:
        a.append(i)
if not a:
    print("none")
else:
    for x in a:
        print(x)
