def binarySearch(list, target):
	left = 0
	right = len(list) - 1  
	#在list[left...right]里查找target，注意是左闭右闭
	while left <= right:
		mid = (right + left) // 2    #取中间元素索引
		if int(list[mid][0]) == target:
			return (''.join(str(i) for i in stu_list[mid]))
		elif target > int(list[mid][0]):
			left = mid + 1     #到list[mid + 1 ...right]里查找
		else:  #target < list[mid]
			right = mid - 1    #到list[left ...mid - 1]里查找
	print(None)    #未找到target元素
stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],

['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],

['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],

['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],

['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
m=int(input())
print(binarySearch(stu_list,m))
