ls = eval(input())
average = sum(ls)/len(ls)
if type(average) == int:
    print(int(average))
else: print('%.2f'% average)
