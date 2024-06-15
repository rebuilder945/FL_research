num_list = eval(input())
zero_list = num_list.count(0)
while num_list.count(0)>=1:
    num_list.remove(0)
for i in range(zero_list):
    num_list.append(0)
print(num_list)


