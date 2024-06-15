def shift(lst):
      del lst[len(lst)-1]
       lst.insert(0,lst[len(lst)-1]
return lst

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

