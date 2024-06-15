lst=input().split(',')
n,m=input().split(",")
n=int(n)
m=int(m)
if n<len(lst):
    a=lst[n]
    for x in range(m):
        lst.append(a)
    lst=list(map(int,lst))		#将列表中的字符串转化为整数形式
    print(lst)
if n>len(lst):
	print('error')
