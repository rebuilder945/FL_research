lst=eval(input())
n,m=input().split(',')		#一行输入多个字符
n=int(n)
m=int(m)
if n<len(lst) and m<len(lst):		#控制输入的n和m在列表的下标内
	if n<m:
		del lst[n:m]
		print(lst)
	else:
		del lst[m+1:n+1]		#包括n但不包括m
		print(lst)
else:
	print('error')

