def shift(lst):
      a=Ist[-1]
      Ist.insert(0,a)
      Ist.pop(-1)

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

