input_list=list(map(int,input().strip('[]').split(',')))
unique_numbers=[]
for num in input_list:
    if input_list.count(num)==1 and num not in unique_numbers:
        unique_numbers.append(num)
unique_numbers.sort(reverse=False)
if not unique_numbers:
    print('false')
else:
    print(','.join(map(str,unique_numbers)))
