list_1 = list(eval(input()))
list_max = max(list_1)
list_min = min(list_1)

while list_max in list_1:
    list_1.remove(list_max)
while list_min in list_1:
    list_1.remove(list_min)
print(list_1)
