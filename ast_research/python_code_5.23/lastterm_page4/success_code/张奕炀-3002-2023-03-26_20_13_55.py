number = eval(input())
sum = sum(number)
if sum%len(number) == 0:
    avg = sum/len(number)
    print(int(avg))
else:
    avg = sum/len(number)
    print('%.2f'%avg)
