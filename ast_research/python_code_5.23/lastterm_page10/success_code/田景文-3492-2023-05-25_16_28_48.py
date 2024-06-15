s = input()
a = []
for x in s:
    if s.count(x) == 1:
        a.append(x)
if a == []:
    print("None")
else:
    print(a[0])
