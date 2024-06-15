ls = eval(input())
average = sum(ls)/len(ls)
if type(average) == int:
    print('%.0f'%average)
else: print('%.2f'% average)
