def shift(lst):
    lst[0],lst[1:len(lst)]=lst[len(lst)-1],lst[0:len(lst)-1]
    global list1
    list1=lst

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

