def shift(lst):
    y=nums[-1]
    del nums[-1]
    nums.insert(0,y)

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

