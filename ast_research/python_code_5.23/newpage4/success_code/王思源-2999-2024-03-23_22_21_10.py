list = list(input().split(" "))
n,m = input().split(" ")
n = int(n)
m = int(m)

for i in range(len(list)):
    temp = list[n]
    list[n] = list[m]
    list[m] = temp
print(list)
