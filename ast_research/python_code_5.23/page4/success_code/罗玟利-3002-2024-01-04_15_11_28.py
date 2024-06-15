input_list = eval(input().strip())
average = sum(input_list) / len(input_list)
if average.is_integer():
    print(int(average))
else:
    print('{:.2f}'.format(average))


