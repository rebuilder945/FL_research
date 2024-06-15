ls1=eval(input())
if sum(ls1)%len(ls1) == 0:
	print(int(sum(ls1)/len(ls1)))
else:
	print('%.2f'%(sum(ls1)/len(ls1)))

