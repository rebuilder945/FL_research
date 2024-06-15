nums=eval(input())
aver=sum(nums/len(nums))
aver_int=int(aver)
if aver>aver_int:
    print('%.2f' % aver)
else:
    print(aver_int)
