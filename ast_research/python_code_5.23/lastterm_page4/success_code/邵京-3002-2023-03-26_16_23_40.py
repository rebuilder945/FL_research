numbers=eval(input())
average=sum(numbers)/len(numbers)
if type(average)==int:
    print(average)
elif type(average)==float:
    print('%.2f'%average)
else:
    print('Flase')
