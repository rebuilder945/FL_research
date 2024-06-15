lst = eval(input())
ave = sum(lst)/len(lst)
if ave % 1 == 0:
    print(int(ave))
else:
    print('%.2f'%ave)
