def shift(lst):
L1=[lst]
m=L1.pop()
s=L1.insert(0,m)
return s


list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

