def shift(lst):
       list2=[]
       for i in range(len(list1)):
            a=list1[i-1]
            list2.append(a)
            for x in list1:
                  list1.remove(x)
            list1+=list2

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

