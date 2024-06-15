lst=input().split(',')
n,m=eval(input())
if n<len(lst):
    a=lst[n]
    for x in range(m):
        lst.append(a)
    lst=list(map(int,(lst)))		#将列表中的字符串转化为整数形式
    print(lst)
if n>=len(lst):
	print('error')
