ls = eval(input())
a = sum(ls)/len(ls)
if a==int(a):
    print(int(a))
else:
    print('%.2f'%(a))

