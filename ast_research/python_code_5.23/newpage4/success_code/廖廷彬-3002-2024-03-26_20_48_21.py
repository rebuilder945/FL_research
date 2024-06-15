input_list_str = input()
input_list = eval(input_list_str)
avg = sum(input_list) / len(input_list)
if avg.is_integer():
    print(int(avg))
else:
    print('%.2f' % avg)
