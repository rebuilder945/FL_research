list = eval(input())


re_list = []
zero_count = 0
for i in range(len(list)):
    if(list[i] != 0):
        re_list.append(list[i])
    else:
        zero_count = zero_count + 1

for i in range(zero_count):
    re_list.append(0)

print(re_list)
