ls = eval(input())
average = sum(ls)/len(ls)
if type(average) == int:
    print('%d'%average)
else: print('%.2f'% average)
