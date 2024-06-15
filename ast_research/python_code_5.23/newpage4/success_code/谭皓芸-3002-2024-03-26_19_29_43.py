num_list = eval(input())
avg = sum(num_list) / len(num_list)

if avg.is_integer():
    print(int(avg))
else:
    print("{:.2f}".format(avg))
