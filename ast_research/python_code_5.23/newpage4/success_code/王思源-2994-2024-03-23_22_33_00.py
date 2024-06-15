list = list(input().split(","))
n,m = eval(input())


list_int = []
for i in range(len(list)):
    list_int.append(int(list[i]))

for i in range(m):
    list_int.append(list_int[n])
print(list_int)
