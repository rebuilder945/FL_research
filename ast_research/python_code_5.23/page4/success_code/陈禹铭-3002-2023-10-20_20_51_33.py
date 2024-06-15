nums=eval(input())
average=sum(nums)/len(nums)
if average.is_integer():
    print(int(average))
else:
    prit(f'{average:.2f}')

