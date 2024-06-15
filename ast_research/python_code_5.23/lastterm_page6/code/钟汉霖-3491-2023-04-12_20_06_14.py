def shift(lst):
n=list.pop()
list.insert(0,n)
return list

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

