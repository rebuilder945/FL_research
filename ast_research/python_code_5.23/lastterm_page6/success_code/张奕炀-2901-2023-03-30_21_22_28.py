list0 = []
while True:
    number = input()
    if number == "#":
        break
    list0.append(int(number))
n = len(list0)
s = 0
for i in range(len(list0)):
    s = s + list0[i]
print(n,end=" ")
print(s)
