list_a = input().split(",")
list_b = eval(input())
i = len(list_a)
list_c = []
for x in range(0,i):
    list_c.append([list_a[x],list_b[x]])
print(list_c)


