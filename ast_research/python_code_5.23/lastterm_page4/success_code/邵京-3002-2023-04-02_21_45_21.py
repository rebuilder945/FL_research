numbers=eval(input())
average=sum(numbers)/len(numbers)
if int(average)==average:
    print(int(average))
else:
    print('%.2f'%average)




