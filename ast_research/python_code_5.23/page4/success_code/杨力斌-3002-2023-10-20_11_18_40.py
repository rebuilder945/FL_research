lst = eval(input())
average = sum(lst)/len(lst)
if average - round(average) != 0:
    print('%.2f'%average)
else:
    print(int(average))
